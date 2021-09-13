
from django.urls import path 
from .views import *




urlpatterns = [
        path('' , home , name="base"),
        path('login/' , login_view , name="login_view"),
        path('register/' , register_view , name="register_view"),
        path('add_blog/' , add_blog, name="add_blog")


]