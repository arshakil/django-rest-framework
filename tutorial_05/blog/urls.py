from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail, APIRoot, CategoryList, CategoryDetail

urlpatterns = [
	path('', APIRoot.as_view()),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='single-post'),

    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='single-category'),

    path('users/', UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', UserDetail.as_view(), name='single-user'),
]
