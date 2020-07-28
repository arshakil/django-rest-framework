from django.db import models

# Create your models here.

class Category(models.Model):  
    title = models.CharField(max_length=200)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']