from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
        
    """
    Custom administration interface for the CustomUser model.
    Extends Django's built-in UserAdmin with additional fields and customization.
    """   
    # ==================== LIST VIEW CONFIGURATION ====================
    # Fields to display in the main list view of the admin panel
    
    list_display = ( 'email', 'id' , 'first_name', 'last_name', 'phone_number', 'role', 
                   'is_verified', 'is_active', 'is_staff', 'profile_image_preview')
    list_filter = ('role', 'is_verified', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    readonly_fields = (  'id' ,'created_at', 'updated_at', 'last_login', 'profile_image_preview')
    
    # Organization of fields in the user detail/edit form
    fieldsets = (
        
        
        (None, {'fields': ('email', 'id', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image')}),
        ('Permissions', {'fields': ('role', 'is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at', 'profile_image_preview')}),
    )
    
    # ==================== ADD/CREATE VIEW CONFIGURATION ====================
    # Fields to display when creating a new user (different from edit view)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # CSS class for wider form layout
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 
                      'phone_number', 'role'),
        }),
    )

    #CUSTOM METHODS

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.profile_image.url)
        return "No Image"
    profile_image_preview.short_description = 'Profile Image'