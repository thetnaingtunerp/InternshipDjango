from django.db import models

# Create your models here.
# Fashoin, Shoes, Cosmetic
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img')
    price = models.PositiveIntegerField()
    dis_price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.item_name
    
class Cart(models.Model):
    total_amount = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"invoice no -{self.cart} --- {self.product}"
    