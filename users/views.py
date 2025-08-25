from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from .models import CustomUser
from .serializers import (CustomUserSerializer, UserProfileUpdateSerializer, 
                         ProfileImageSerializer)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = CustomUserSerializer(request.user, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserProfileUpdateSerializer(
            request.user, 
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            # Return full user data after update
            user_serializer = CustomUserSerializer(request.user, context={'request': request})
            return Response(user_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileImageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def put(self, request):
        serializer = ProfileImageSerializer(
            request.user, 
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            user_serializer = CustomUserSerializer(request.user, context={'request': request})
            return Response(user_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        if request.user.profile_image:
            request.user.profile_image.delete()
            request.user.profile_image = None
            request.user.save()
        user_serializer = CustomUserSerializer(request.user, context={'request': request})
        return Response(user_serializer.data)

class UserListView(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response(
                {'detail': 'Successfully logged out.'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def check_phone_number(request, phone_number):
    """Check if phone number is already in use"""
    exists = CustomUser.objects.filter(phone_number=phone_number).exclude(id=request.user.id).exists()
    return Response({'exists': exists})