from rest_framework import serializers
from users.models import CustomUser
from rent_user.models import Notification, Message
from rent_add.models import RentAdvertisement, RentRequest ,AdvertisementImage, FavoriteAdvertisement, Review
from rent_type.models import Category, Amenity




class CategorySerializer(serializers.ModelSerializer):
    advertisement_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'advertisement_count']
    
    def get_advertisement_count(self, obj):
        return obj.rentadvertisement_set.filter(status='approved', is_available=True).count()

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'description']