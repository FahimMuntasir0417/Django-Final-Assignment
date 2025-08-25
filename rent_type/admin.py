from django.contrib import admin
from .models import Category, Amenity
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'advertisement_count']
    search_fields = ['name']
    
    def advertisement_count(self, obj):
        return obj.rentadvertisement_set.count()
    advertisement_count.short_description = 'Ads Count'

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


