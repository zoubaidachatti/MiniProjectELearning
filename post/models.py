from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    state=models.CharField(max_length=4,default='No')
    logo=models.ImageField(upload_to='images')
    category=models.CharField(max_length=100)