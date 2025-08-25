from django.db import models
from django.conf import settings
from rent_add.models import RentAdvertisement, RentRequest
from django.utils import timezone
# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('rent_request', 'Rent Request'),
        ('request_accepted', 'Request Accepted'),
        ('request_rejected', 'Request Rejected'),
        ('ad_approved', 'Advertisement Approved'),
        ('ad_rejected', 'Advertisement Rejected'),
        ('new_review', 'New Review'),
        ('message', 'Message'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    related_advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, null=True, blank=True)
    related_request = models.ForeignKey(RentRequest, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.notification_type}"

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.username} to {self.recipient.username}: {self.subject}"