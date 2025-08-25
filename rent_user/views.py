from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .models import Notification, Message
from .serializers import (
    NotificationSerializer, 
    MessageSerializer, 
    MessageCreateSerializer
)









# class NotificationViewSet(viewsets.ModelViewSet):
#     serializer_class = NotificationSerializer
#     permission_classes = [IsAuthenticated]
#     # lookup_field = 'id'
    
#     def get_queryset(self):
#         return Notification.objects.filter(user=self.request.user).order_by('-created_at')
    
#     @action(detail=True, methods=['post'])
#     def mark_as_read(self, request, pk=None):
#         notification = self.get_object()
#         notification.is_read = True
#         notification.save()
#         return Response({'status': 'notification marked as read'})
    
#     @action(detail=False, methods=['post'])
#     def mark_all_as_read(self, request):
#         Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
#         return Response({'status': 'all notifications marked as read'})

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        # Only return notifications for the current user
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Message.objects.filter(
            Q(sender=self.request.user) | Q(recipient=self.request.user)
        ).order_by('-created_at')
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return MessageCreateSerializer
        return MessageSerializer
    
    def perform_create(self, serializer):
        message = serializer.save(sender=self.request.user)
        
        # Create notification for the recipient
        Notification.objects.create(
            user=message.recipient,
            notification_type='message',
            message=f'You have a new message from {self.request.user.username}.',
            related_advertisement=message.advertisement
        )