from core.models import (
    BannerImages, Category, SubCategory, Product, ProducInfo, FavoriteList, Basket, HelpForm, 
    Location, FAQ, SocialMedia, ShippingAndReturn, TermAndCondition, SiteSettings)
from core.api.serializer import (
    UserCreateSerializer, BannerImageSerializer, CategorySerializer, ProductSerializer,
    ProductRetrieveSerializer, FavoriteListCreateSerializer, FavoriteListSerializer,
    BasketSerializer, BasketCreateSerializer, HelpFormSerializer, LocationSerializer, FAQSerializer,
    SocialMediaSerializer, ShippingAndReturnSerializer, TermAndConditionSerializer, SiteSettingsSerializer)
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class BannerImageListAPIView(ListAPIView):
    queryset = BannerImages.objects.all()
    serializer_class = BannerImageSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    lookup_field = "id"

class UserFavoriteListListAPİView(ListAPIView):
    def get_queryset(self):
        return FavoriteList.objects.filter(
            user = self.request.user
        )
    serializer_class = FavoriteListSerializer

class FavoriteListListAPIView(ListAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = (IsAdminUser, )

class FavoriteListCreateAPIView(CreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class BasketListAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAdminUser, )

class UserBasketListAPIView(ListAPIView):
    def get_queryset(self):
        return Basket.objects.filter(
            user = self.request.user
        )
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated, )

class BasketCreateAPIView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HelpFormCreateAPIView(CreateAPIView):
    queryset = HelpForm.objects.all()
    serializer_class = HelpFormSerializer

class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FAQListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class ShippingAndReturnListAPIView(ListAPIView):
    queryset = ShippingAndReturn.objects.all()
    serializer_class = ShippingAndReturnSerializer

class TermAndConditionListAPIView(ListAPIView):
    queryset = TermAndCondition.objects.all()
    serializer_class = TermAndConditionSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer