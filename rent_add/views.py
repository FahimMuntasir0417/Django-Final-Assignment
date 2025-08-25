from rest_framework.exceptions import ValidationError
from rest_framework import generics, status, filters, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Count, Avg, F
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from rent_api.permissions import IsOwnerOrAdmin

#import model from other apps

from rent_add.models import (
    RentAdvertisement, 
    RentRequest, FavoriteAdvertisement, Review,AdvertisementImage
)

from rent_type.models import (
    Category
    
)

from rent_user.models import (
     Notification
)

from rent_add.serializers import (
     RentAdvertisementListSerializer, RentRequestUpdateSerializer,
    FavoriteAdvertisementCreateSerializer,FavoriteAdvertisementSerializer,AdvertisementImageSerializer,
    ReviewSerializer,RentAdvertisementCreateSerializer,RentAdvertisementDetailSerializer,RentRequestSerializer )
# from rent_type.serializers import CategorySerializer, AmenitySerializer
# from rent_user.serializers import( UserSerializer, NotificationSerializer,
# MessageSerializer, MessageCreateSerializer,RentRequestSerializer )  



from rent_api.permissions import IsOwnerOrReadOnly, IsAdvertisementOwner
from rent_api.filters import RentAdvertisementFilter
from rent_api.pagination import CustomPagination


class RentAdvertisementViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RentAdvertisementFilter
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price', 'created_at', 'area', 'bedrooms', 'views_count']
    ordering = ['-created_at']
    pagination_class = CustomPagination
    
    def get_queryset(self):
        if self.request.user.is_staff:
            # Admins can see all ads
            queryset = RentAdvertisement.objects.all()
        else:
            # Regular users can only see approved and available ads
            queryset = RentAdvertisement.objects.filter(status='approved', is_available=True)
        
        # For detail view, we want to include all ads (permissions handled elsewhere)
        if self.action == 'retrieve':
            return RentAdvertisement.objects.all()
            
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return RentAdvertisementListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return RentAdvertisementCreateSerializer
        return RentAdvertisementDetailSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'my_advertisements']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']: 
            permission_classes = [IsOwnerOrReadOnly]
        elif self.action in ['approve', 'reject']:
            permission_classes = [IsAdminUser]
        elif self.action in ['destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    

    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increment_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_advertisements(self, request):
        ads = RentAdvertisement.objects.filter(owner=request.user)
        page = self.paginate_queryset(ads)
        serializer = RentAdvertisementListSerializer(page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        advertisement = self.get_object()
        advertisement.status = 'approved'
        advertisement.save()
        
        # Create notification for the owner
        Notification.objects.create(
            user=advertisement.owner,
            notification_type='ad_approved',
            message=f'Your advertisement "{advertisement.title}" has been approved and is now live.',
            related_advertisement=advertisement
        )
        
        return Response({'status': 'advertisement approved'})
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        advertisement = self.get_object()
        advertisement.status = 'rejected'
        advertisement.save()
        
        # Create notification for the owner
        Notification.objects.create(
            user=advertisement.owner,
            notification_type='ad_rejected',
            message=f'Your advertisement "{advertisement.title}" has been rejected.',
            related_advertisement=advertisement
        )
        
        return Response({'status': 'advertisement rejected'})
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        advertisement = self.get_object()
        favorite, created = FavoriteAdvertisement.objects.get_or_create(
            user=request.user,
            advertisement=advertisement,
            defaults={'notes': request.data.get('notes', '')}
        )
        
        if not created:
            return Response(
                {'error': 'This advertisement is already in your favorites'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = FavoriteAdvertisementSerializer(favorite, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated])
    def unfavorite(self, request, pk=None):
        advertisement = self.get_object()
        favorite = get_object_or_404(
            FavoriteAdvertisement, 
            user=request.user, 
            advertisement=advertisement
        )
        favorite.delete()
        return Response({'status': 'removed from favorites'})

class RentRequestViewSet(viewsets.ModelViewSet):
    serializer_class = RentRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return RentRequest.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return RentRequestUpdateSerializer
        return RentRequestSerializer
    
    def perform_create(self, serializer):
        advertisement_id = self.request.data.get('advertisement')
        advertisement = RentAdvertisement.objects.get(id=advertisement_id)
        
        # Check if advertisement is available for rent requests
        if advertisement.status != 'approved' or not advertisement.is_available:
            return Response(
                {'error': 'This advertisement is not available for rent requests'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if user already sent a request
        if RentRequest.objects.filter(advertisement=advertisement, user=self.request.user).exists():
            return Response(
                {'error': 'You have already sent a rent request for this advertisement'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        rent_request = serializer.save(user=self.request.user, advertisement=advertisement)
        
        # Create notification for the advertisement owner
        Notification.objects.create(
            user=advertisement.owner,
            notification_type='rent_request',
            message=f'{self.request.user.username} has sent a rent request for your advertisement "{advertisement.title}".',
            related_advertisement=advertisement,
            related_request=rent_request
        )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdvertisementOwner])
    def accept(self, request, pk=None):
        rent_request = self.get_object()
        
        # Check if the advertisement already has an accepted request
        if RentRequest.objects.filter(
            advertisement=rent_request.advertisement, 
            status='accepted'
        ).exists():
            return Response(
                {'error': 'This advertisement already has an accepted rent request'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        rent_request.status = 'accepted'
        rent_request.save()
        
        # Mark advertisement as rented and unavailable for further requests
        advertisement = rent_request.advertisement
        advertisement.status = 'rented'
        advertisement.is_available = False
        advertisement.save()
        
        # Reject all other pending requests for this advertisement
        RentRequest.objects.filter(
            advertisement=advertisement, 
            status='pending'
        ).update(status='rejected')
        
        # Create notification for the requester
        Notification.objects.create(
            user=rent_request.user,
            notification_type='request_accepted',
            message=f'Your rent request for "{advertisement.title}" has been accepted.',
            related_advertisement=advertisement,
            related_request=rent_request
        )
        
        return Response({'status': 'rent request accepted'})
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdvertisementOwner])
    def reject(self, request, pk=None):
        rent_request = self.get_object()
        rent_request.status = 'rejected'
        rent_request.save()
        
        # Create notification for the requester
        Notification.objects.create(
            user=rent_request.user,
            notification_type='request_rejected',
            message=f'Your rent request for "{rent_request.advertisement.title}" has been rejected.',
            related_advertisement=rent_request.advertisement,
            related_request=rent_request
        )
        
        return Response({'status': 'rent request rejected'})



# class FavoriteAdvertisementViewSet(viewsets.ModelViewSet):
#     serializer_class = FavoriteAdvertisementSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return FavoriteAdvertisement.objects.filter(user=self.request.user)
    
#     def get_serializer_class(self):
#         if self.action in ['create', 'update', 'partial_update']:
#             return FavoriteAdvertisementCreateSerializer
#         return FavoriteAdvertisementSerializer
    
#     def perform_create(self, serializer):
#         advertisement_id = self.request.data.get('advertisement')
#         advertisement = RentAdvertisement.objects.get(id=advertisement_id)
        
#         # Check if already favorited
#         if FavoriteAdvertisement.objects.filter(
#             user=self.request.user, 
#             advertisement=advertisement
#         ).exists():
#             return Response(
#                 {'error': 'This advertisement is already in your favorites'}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         serializer.save(user=self.request.user, advertisement=advertisement)


class FavoriteAdvertisementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = FavoriteAdvertisementSerializer
    lookup_field = 'advertisement__id'  # allows access via advertisement ID

    def get_queryset(self):
        # Only favorites of the current user
        return FavoriteAdvertisement.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FavoriteAdvertisementCreateSerializer
        return FavoriteAdvertisementSerializer

    def perform_create(self, serializer):
        advertisement_id = self.request.data.get('advertisement')
        try:
            advertisement = RentAdvertisement.objects.get(id=advertisement_id)
        except RentAdvertisement.DoesNotExist:
            raise ValidationError({'error': 'Advertisement not found'})

        # Check if already favorited
        if FavoriteAdvertisement.objects.filter(user=self.request.user, advertisement=advertisement).exists():
            raise ValidationError({'error': 'This advertisement is already in your favorites'})

        serializer.save(user=self.request.user, advertisement=advertisement)

    def perform_destroy(self, instance):
        # Optional: only owner can delete
        if instance.user != self.request.user:
            raise ValidationError({'error': 'You do not have permission to delete this favorite'})
        instance.delete()




class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        advertisement_id = self.request.data.get('advertisement')
        advertisement = RentAdvertisement.objects.get(id=advertisement_id)
        
        # Check if user already reviewed this advertisement
        if Review.objects.filter(
            user=self.request.user, 
            advertisement=advertisement
        ).exists():
            return Response(
                {'error': 'You have already reviewed this advertisement'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        review = serializer.save(user=self.request.user, advertisement=advertisement)
        
        # Create notification for the advertisement owner
        Notification.objects.create(
            user=advertisement.owner,
            notification_type='new_review',
            message=f'{self.request.user.username} has reviewed your advertisement "{advertisement.title}".',
            related_advertisement=advertisement
        )



@api_view(['GET'])
@permission_classes([IsAdminUser])
def advertisement_statistics(request):
    # Current month statistics
    current_month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    current_month_ads = RentAdvertisement.objects.filter(created_at__gte=current_month_start)
    
    # Last month statistics
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    last_month_ads = RentAdvertisement.objects.filter(
        created_at__gte=last_month_start, 
        created_at__lte=last_month_end
    )
    
    # Total statistics
    total_ads = RentAdvertisement.objects.count()
    
    # Popular categories
    popular_categories = Category.objects.annotate(
        ad_count=Count('rentadvertisement')
    ).order_by('-ad_count')[:5]
    
    data = {
        'current_month': {
            'total': current_month_ads.count(),
            'approved': current_month_ads.filter(status='approved').count(),
            'pending': current_month_ads.filter(status='pending').count(),
            'rejected': current_month_ads.filter(status='rejected').count(),
            'rented': current_month_ads.filter(status='rented').count(),
        },
        'last_month': {
            'total': last_month_ads.count(),
            'approved': last_month_ads.filter(status='approved').count(),
            'pending': last_month_ads.filter(status='pending').count(),
            'rejected': last_month_ads.filter(status='rejected').count(),
            'rented': last_month_ads.filter(status='rented').count(),
        },
        'all_time': {
            'total': total_ads,
            'approved': RentAdvertisement.objects.filter(status='approved').count(),
            'pending': RentAdvertisement.objects.filter(status='pending').count(),
            'rejected': RentAdvertisement.objects.filter(status='rejected').count(),
            'rented': RentAdvertisement.objects.filter(status='rented').count(),
        },
        'popular_categories': [
            {'name': cat.name, 'count': cat.ad_count} for cat in popular_categories
        ]
    }
    
    return Response(data)

class AdvertisementImageViewSet(viewsets.ModelViewSet):
    queryset = AdvertisementImage.objects.all()
    serializer_class = AdvertisementImageSerializer