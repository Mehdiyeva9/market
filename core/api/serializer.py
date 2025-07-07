from rest_framework import serializers
from core.models import (
    BannerImages, Category, SubCategory, Product, ProducInfo, FavoriteList, Basket, HelpForm, 
    Location, FAQ, SocialMedia, ShippingAndReturn, TermAndCondition, SiteSettings)
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        validate_password(attrs["password"])
        return attrs
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username = username,
            password = password
        )
        return user

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = BannerImages
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = SubCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    class Meta:
        models = Category
        fields = "__all__"

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        models = ProducInfo
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = ("image", "name", "price", "discount_price")

class ProductRetrieveSerializer(serializers.ModelSerializer):
    info = ProductInfoSerializer()
    class Meta:
        models = Product
        fields = "__all__"

class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = "__all__"

class FavoriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ("product", )

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"

class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("product", )

class HelpFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpForm
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class ShippingAndReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAndReturn
        fields = "__all__"

class TermAndConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermAndCondition
        fields = "__all__"
    
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"