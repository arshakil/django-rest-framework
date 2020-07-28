from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/', post_detail, name='post_detail'),
]
