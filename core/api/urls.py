from django.conf import urls
from core.api import views
from django.urls import path

urlpatterns = {
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('bannerimage-list/', views.BannerImageListAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-retrieve/<id>', views.ProductRetrieveAPIView.as_view()),
    path('user-favorite-list/', views.UserFavoriteListListAPİView.as_view()),
    path('favorite-list/', views.FavoriteListListAPIView.as_view()),
    path('favoritelist-create/', views.FavoriteListCreateAPIView.as_view()),
    path('user-basket-list/', views.UserBasketListAPIView.as_view()),
    path('basket-list/', views.BasketListAPIView.as_view()),
    path('basket-create/', views.BasketCreateAPIView.as_view()),
    path('helpform-create/', views.HelpFormCreateAPIView.as_view()),
    path('location-list/', views.LocationListAPIView.as_view()),
    path('faq-list/', views.FAQListAPIView.as_view()),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view()),
    path('shippingandreturn-list/', views.ShippingAndReturnListAPIView.as_view()),
    path('termandcondition-list/', views.TermAndConditionListAPIView.as_view()),
    path('sitesettings-list/', views.SiteSettingsListAPIView.as_view())
}