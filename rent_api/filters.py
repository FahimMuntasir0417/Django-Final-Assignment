# filters.py
import django_filters
from  rent_add.models import RentAdvertisement

class RentAdvertisementFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_bedrooms = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='gte')
    max_bedrooms = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='lte')
    min_bathrooms = django_filters.NumberFilter(field_name='bathrooms', lookup_expr='gte')
    max_bathrooms = django_filters.NumberFilter(field_name='bathrooms', lookup_expr='lte')
    min_area = django_filters.NumberFilter(field_name='area', lookup_expr='gte')
    max_area = django_filters.NumberFilter(field_name='area', lookup_expr='lte')
    
    class Meta:
        model = RentAdvertisement
        fields = [
            'category', 'bedrooms', 'bathrooms', 'price', 'area',
            'min_price', 'max_price', 'min_bedrooms', 'max_bedrooms',
            'min_bathrooms', 'max_bathrooms', 'min_area', 'max_area'
        ]