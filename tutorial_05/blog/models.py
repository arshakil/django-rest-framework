from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):  
    title = models.CharField(max_length=200)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return '%d: %s' % (self.id, self.title)

    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, default="")
    body = models.TextField()   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']