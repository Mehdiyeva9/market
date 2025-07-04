from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "SubCategories"

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="market_img/")
    name = models.CharField(max_length=50)
    stock_number = models.CharField(max_length=20)
    content = models.TextField()
    price = models.FloatField(default=0)
    discount_price = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    number_of_sales = models.IntegerField(default=0)
    raiting = models.FloatField(default=0)
    discount_status = models.BooleanField(default=False)

    def __str__(self):
            return self.name

class ProducInfo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product infos")
    
    def __str__(self):
        return self.title

class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favori_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favori_items')

    def __str__(self):
        return self.product
    
class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="basket_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_basket")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product
    
class HelpForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=256)
    phone = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.first_name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    adress = models.TextField()
    number = models.CharField(max_length=15)
    icon = models.ImageField(upload_to="market_img/")

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    icon = models.ImageField(upload_to="market_img/")
    link = models.URLField(max_length=200)

    def __str__(self):
        return "Social Media"
    
class ShippingAndReturn(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class TermAndCondition(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title