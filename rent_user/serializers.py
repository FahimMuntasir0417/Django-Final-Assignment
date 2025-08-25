from rest_framework import serializers
from users.models import CustomUser
from rent_user.models import Notification, Message
from rent_add.models import RentAdvertisement, RentRequest ,AdvertisementImage, FavoriteAdvertisement, Review
from rent_type.models import Category, Amenity




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name']


# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = [
#             'id', 'notification_type', 'message', 'related_advertisement', 
#             'related_request', 'is_read', 'created_at'
#         ]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('user',)  # Make user read-only

    def create(self, validated_data):
        # Automatically set the user from the request
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)




class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    advertisement_title = serializers.CharField(source='advertisement.title', read_only=True)
    
    class Meta:
        model = Message
        fields = [
            'id', 'sender', 'recipient', 'advertisement', 'advertisement_title',
            'subject', 'content', 'is_read', 'created_at'
        ]
        read_only_fields = ['sender']

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['recipient', 'advertisement', 'subject', 'content']