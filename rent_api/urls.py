# from django.urls import path, include
# from rest_framework_nested import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from django.conf import settings
# from django.conf.urls.static import static
# from users.views import (UserProfileView, UserLogoutView, UserListView, 
#                    ProfileImageView, check_phone_number)


# from rent_add.views import RentAdvertisementViewSet, RentRequestViewSet, AdvertisementImageViewSet, FavoriteAdvertisementViewSet, ReviewViewSet
# from rent_type.views import CategoryViewSet, AmenityViewSet 
# from rent_user.views import NotificationViewSet, MessageViewSet



# router = routers.DefaultRouter()
# router.register(r'categories', views.CategoryViewSet)
# router.register(r'amenities', views.AmenityViewSet)
# router.register(r'advertisements', views.RentAdvertisementViewSet, basename='advertisement')
# router.register(r'rent-requests', views.RentRequestViewSet, basename='rentrequest')
# router.register(r'favorites', views.FavoriteAdvertisementViewSet, basename='favorite')
# router.register(r'reviews', views.ReviewViewSet, basename='review')
# router.register(r'notifications', views.NotificationViewSet, basename='notification')
# router.register(r'messages', views.MessageViewSet, basename='message')

# # Nested router for advertisement images
# advertisements_router = routers.NestedDefaultRouter(router, r'advertisements', lookup='advertisement')
# advertisements_router.register(r'images', views.AdvertisementImageViewSet, basename='advertisement-images')
# advertisements_router.register(r'reviews', views.ReviewViewSet, basename='advertisement-reviews')
# advertisements_router.register(r'rent-requests', views.RentRequestViewSet, basename='advertisement-rent-requests')


# urlpatterns = [
#     # Djoser endpoints
#     path('auth/', include('djoser.urls')),
    
#     # JWT endpoints
#     path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
#     path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
#     path('auth/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    
#     # Custom endpoints
#     path('auth/logout/', UserLogoutView.as_view(), name='logout'),
#     path('profile/', UserProfileView.as_view(), name='user-profile'),
#     path('profile/image/', ProfileImageView.as_view(), name='profile-image'),
#     path('profile/check-phone/<str:phone_number>/', check_phone_number, name='check-phone'),
#     path('users/', UserListView.as_view(), name='user-list'),
    
    
    
    
#     path('', include(router.urls)),
#     path('', include(advertisements_router.urls)),
#     path('statistics/', views.advertisement_statistics, name='advertisement-statistics'),
# ]

# # Serve media files in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    UserProfileView, UserLogoutView, UserListView,
    ProfileImageView, check_phone_number
)
from rent_add.views import (
    RentAdvertisementViewSet, RentRequestViewSet, AdvertisementImageViewSet,
    FavoriteAdvertisementViewSet, ReviewViewSet, advertisement_statistics
)
from rent_type.views import CategoryViewSet, AmenityViewSet
from rent_user.views import NotificationViewSet, MessageViewSet


# Main router
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'advertisements', RentAdvertisementViewSet, basename='advertisement')
router.register(r'rent-requests', RentRequestViewSet, basename='rentrequest')
router.register(r'favorites', FavoriteAdvertisementViewSet, basename='favorite')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'messages', MessageViewSet, basename='message')


# Nested router for advertisement images, reviews, and rent requests
advertisements_router = routers.NestedDefaultRouter(router, r'advertisements', lookup='advertisement')
advertisements_router.register(r'images', AdvertisementImageViewSet, basename='advertisement-images')
advertisements_router.register(r'reviews', ReviewViewSet, basename='advertisement-reviews')
advertisements_router.register(r'rent-requests', RentRequestViewSet, basename='advertisement-rent-requests')


# URL patterns
urlpatterns = [
    # Djoser auth endpoints
    path('auth/', include('djoser.urls')),

    # JWT endpoints
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    # Custom user endpoints
    path('auth/logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/image/', ProfileImageView.as_view(), name='profile-image'),
    path('profile/check-phone/<str:phone_number>/', check_phone_number, name='check-phone'),
    path('users/', UserListView.as_view(), name='user-list'),

    # Routers
    path('', include(router.urls)),
    path('', include(advertisements_router.urls)),

    # Advertisement statistics
    path('statistics/', advertisement_statistics, name='advertisement-statistics'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
