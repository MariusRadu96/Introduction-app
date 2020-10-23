from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name', 'slug')



class LiveGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = LiveGame
        fields = ('name', 'game_type', 'slug', 'vendor' , 'categories', 'dealer_gender', 'dealer_language') 


class SlotGameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SlotGame
        fields = ('name', 'game_type', 'slug', 'vendor' , 'categories', 'jackpot', 'jackpot_currency') 

