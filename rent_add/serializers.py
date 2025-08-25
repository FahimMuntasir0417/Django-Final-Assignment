
from rest_framework import serializers
from users.models import CustomUser
from rent_user.models import Notification, Message
from rent_add.models import RentAdvertisement, RentRequest ,AdvertisementImage, FavoriteAdvertisement, Review
from rent_type.models import Category, Amenity
from rent_user.serializers import UserSerializer
from rent_type.serializers import AmenitySerializer, CategorySerializer









class AdvertisementImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    # image = serializers.ImageField(use_url=True)
    class Meta:
        model = AdvertisementImage
        fields = ['id', 'image', 'is_primary', 'uploaded_at']

class RentAdvertisementListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    # primary_image = serializers.SerializerMethodField()
    primary_image = serializers.ImageField()

    category_name = serializers.CharField(source='category.name', read_only=True)
    is_favorited = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = RentAdvertisement
        fields = [
            'id', 'title', 'price', 'location', 'area', 
            'bedrooms', 'bathrooms', 'category', 'category_name', 'owner', 
            'status', 'created_at', 'is_available', 'primary_image',
            'is_favorited', 'average_rating', 'review_count', 'views_count'
        ]
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return AdvertisementImageSerializer(primary_image).data
        first_image = obj.images.first()
        if first_image:
            return AdvertisementImageSerializer(first_image).data
        return None
    
    def get_is_favorited(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.favorited_by.filter(user=user).exists()
        return False
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()

class RentAdvertisementDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = AdvertisementImageSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    is_favorited = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    similar_ads = serializers.SerializerMethodField()
    
    class Meta:
        model = RentAdvertisement
        fields = [
            'id', 'title', 'description', 'price', 'location', 'latitude', 'longitude',
            'area', 'bedrooms', 'bathrooms', 'category', 'category_name', 'amenities',
            'owner', 'status', 'created_at', 'updated_at', 'is_available', 'images',
            'is_favorited', 'average_rating', 'review_count', 'available_from',
            'minimum_lease', 'deposit', 'contact_phone', 'contact_email', 'views_count',
            'similar_ads'
        ]
    
    def get_is_favorited(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.favorited_by.filter(user=user).exists()
        return False
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()
    
    def get_similar_ads(self, obj):
        # Get similar ads based on category and location
        similar_ads = RentAdvertisement.objects.filter(
            category=obj.category, 
            location__icontains=obj.location.split(',')[0],  # First part of location
            status='approved',
            is_available=True
        ).exclude(id=obj.id)[:4]
        return RentAdvertisementListSerializer(similar_ads, many=True, context=self.context).data

class RentAdvertisementCreateSerializer(serializers.ModelSerializer):
    images = AdvertisementImageSerializer(many=True, required=False)
    
    class Meta:
        model = RentAdvertisement
        fields = [
            'title', 'description', 'price', 'location', 'latitude', 'longitude',
            'area', 'bedrooms', 'bathrooms', 'category', 'amenities', 'available_from',
            'minimum_lease', 'deposit', 'contact_phone', 'contact_email', 'images'
        ]
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        amenities_data = validated_data.pop('amenities', [])
        
        advertisement = RentAdvertisement.objects.create(
            **validated_data, 
            owner=self.context['request'].user
        )
        
        # Add amenities
        advertisement.amenities.set(amenities_data)
        
        # Add images
        for image_data in images_data:
            AdvertisementImage.objects.create(
                advertisement=advertisement, 
                **image_data
            )
        
        return advertisement

class RentRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    advertisement_title = serializers.CharField(source='advertisement.title', read_only=True)
    # advertisement_image = serializers.SerializerMethodField()
    advertisement_image = serializers.ImageField()

    
    class Meta:
        model = RentRequest
        fields = [
            'id', 'advertisement', 'advertisement_title', 'advertisement_image', 
            'user', 'message', 'status', 'move_in_date', 'lease_duration', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'status']
    
    def get_advertisement_image(self, obj):
        primary_image = obj.advertisement.images.filter(is_primary=True).first()
        if primary_image:
            return AdvertisementImageSerializer(primary_image).data
        first_image = obj.advertisement.images.first()
        if first_image:
            return AdvertisementImageSerializer(first_image).data
        return None

class RentRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = ['status', 'message']

class FavoriteAdvertisementSerializer(serializers.ModelSerializer):
    advertisement = RentAdvertisementListSerializer(read_only=True)
    
    class Meta:
        model = FavoriteAdvertisement
        fields = ['id', 'advertisement', 'notes', 'created_at']

class FavoriteAdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAdvertisement
        fields = ['advertisement', 'notes']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_has_reviewed = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = [
            'id', 'advertisement', 'user', 'rating', 'comment', 
            'created_at', 'updated_at', 'is_verified', 'user_has_reviewed'
        ]
        read_only_fields = ['user', 'is_verified']
    
    def get_user_has_reviewed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Review.objects.filter(
                advertisement=obj.advertisement, 
                user=request.user
            ).exists()
        return False