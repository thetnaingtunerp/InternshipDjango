from django.urls import path
from .views import *
urlpatterns = [
    path('myview/', Myview.as_view(), name='Myview'),
]