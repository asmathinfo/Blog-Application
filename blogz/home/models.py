from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to='blogz')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=true)
    



