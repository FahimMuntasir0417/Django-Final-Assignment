
from rest_framework import viewsets
from .models import Category, Amenity
from .serializers import CategorySerializer, AmenitySerializer
from django.db.models import Count
from rent_api import permissions



# class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Category.objects.annotate(ad_count=Count('rentadvertisement'))
#     serializer_class = CategorySerializer
#     pagination_class = None
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.annotate(ad_count=Count('rentadvertisement'))
    serializer_class = CategorySerializer
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]  # Allow unrestricted access


# class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Amenity.objects.all()
#     serializer_class = AmenitySerializer
#     pagination_class = None
    

class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    pagination_class = None
    
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]  # Allow unrestricted access