from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    written_by =models.CharField(max_length=50)

class Contect(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile =models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    message = models.TextField()