from django.db import models

# Create your models here.


# pip install Pillow

class Myfriend(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=200)
    address = models.TextField()
    emial = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    created = models.DateField()
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_body = models.TextField()
    photo = models.ImageField(upload_to='post_photo')
    created_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    post_body = models.TextField()
    photo1 = models.ImageField(upload_to='bolgphoto')
    photo2 = models.ImageField(upload_to='bolgphoto')
    photo3 = models.ImageField(upload_to='bolgphoto')
    created_date = models.DateField(auto_now=True)
    
    
