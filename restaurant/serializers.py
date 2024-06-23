from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']