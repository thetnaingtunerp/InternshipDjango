from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img')
    price = models.PositiveIntegerField()

class CartItem(models.Model):
    items = models.ForeignKey(Category, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now_add=True)