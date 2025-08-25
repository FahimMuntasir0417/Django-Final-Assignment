from django.contrib import admin
from .models import RentAdvertisement, AdvertisementImage, RentRequest, FavoriteAdvertisement, Review
# Register your models here.


@admin.register(RentAdvertisement)
class RentAdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'location', 'price', 'status', 'created_at', 'views_count']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at', 'updated_at', 'views_count']
    filter_horizontal = ['amenities']

@admin.register(AdvertisementImage)
class AdvertisementImageAdmin(admin.ModelAdmin):
    list_display = ['advertisement', 'is_primary']
    list_filter = ['is_primary']

@admin.register(RentRequest)
class RentRequestAdmin(admin.ModelAdmin):
    list_display = ['advertisement', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['advertisement__title', 'user__username']

@admin.register(FavoriteAdvertisement)
class FavoriteAdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'advertisement', 'created_at']
    search_fields = ['user__username', 'advertisement__title']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['advertisement', 'user', 'rating', 'created_at', 'is_verified']
    list_filter = ['rating', 'created_at', 'is_verified']
    search_fields = ['advertisement__title', 'user__username']