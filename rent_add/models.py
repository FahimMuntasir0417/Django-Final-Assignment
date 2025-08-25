import uuid
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from rent_type.models import Category, Amenity
from django.conf import settings 
from cloudinary.models import CloudinaryField

# Create your models here.

class RentAdvertisement(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('rented', 'Rented'),
        ('expired', 'Expired'),
    )
    
    
    # UUID field is being be added for more secure identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='advertisements')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    available_from = models.DateField(null=True, blank=True)
    minimum_lease = models.PositiveIntegerField(default=12, help_text="Minimum lease in months")
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField(blank=True)
    views_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.location}"
    
    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])
    
    def is_expired(self):
        # Ads expire after 30 days if not approved or extended
        if self.status in ['approved', 'rented']:
            return False
        return (timezone.now() - self.created_at).days > 30

class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.advertisement.title}"

class RentRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    )
    
    # UUID field is being be added for more secure identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    
    advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, related_name='rent_requests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rent_requests')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    move_in_date = models.DateField(null=True, blank=True)
    lease_duration = models.PositiveIntegerField(default=12, help_text="Lease duration in months")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['advertisement', 'user']
    
    def __str__(self):
        return f"{self.user.username} - {self.advertisement.title}"

class FavoriteAdvertisement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['user', 'advertisement']
    
    def __str__(self):
        return f"{self.user.username} - {self.advertisement.title}"

class Review(models.Model):
    advertisement = models.ForeignKey(RentAdvertisement, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['advertisement', 'user']
    
    def __str__(self):
        return f"{self.user.username} - {self.advertisement.title} - {self.rating} stars"