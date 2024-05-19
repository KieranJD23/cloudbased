from django.db import models
import datetime

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    brand= models.CharField(max_length=100)
    average_cost= models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    date_of_released= models.DateField()
    description= models.CharField(max_length=500, default="", blank=True, null=True)
    photo_of_product= models.ImageField(upload_to="uploads/product/")

    def __str_(self):
        return self.product_name

class Profile(models.Model):
    full_name= models.CharField(max_length=100)
    date_of_birth= models.DateField()
    address=models.CharField(max_length=100)
    city_town=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    photo_of_user= models.ImageField(upload_to="uploads/user/")

    def __str_(self):
        return self.full_name

class Review(models.Model):
    author= models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    Product_rating=models.CharField(max_length=100)
    the_review=models.CharField(max_length=1000)
    date_of_post= models.DateField()
    
    def __str_(self):
        return self.author