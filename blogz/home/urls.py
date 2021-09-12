
from django.urls import path 
from .views import *




urlpatterns = [
        path('' , home , name="base"),
        path('login/' , login_view , name="login_view"),

]