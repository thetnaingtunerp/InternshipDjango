from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('updatecourse/<int:pk>/', updatecourse, name='updatecourse'),
    
    path('login/', loginview, name='loginview'),
]