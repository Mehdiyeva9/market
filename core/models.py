from django.db import models

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