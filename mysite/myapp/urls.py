from django.urls import path
from .views import *

urlpatterns = [
    path('posts/',postdata , name='posts'),
    path('detail/<int:pk>/', postdetail, name='detail'),
    path('create/', createpost, name='createpost'),
    path('createfrom/', createfrom, name = 'createfrom'),
    path('blog/', createblog, name='createblog'),
    path('saveblog/', saveblog, name='saveblog'),
    path('bloglist/', bloglist, name='bloglist'),
    path('blogdetail/<int:pk>/', blogdetail, name='blogdetail'),
    path('deleteblog/<int:pk>/', deleteblog, name='deleteblog'),
    path('update/<int:pk>/', blogupdate, name='blogupdate'),
]