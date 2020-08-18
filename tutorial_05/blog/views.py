

#  API using class-based views

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# 


#  for generics class based Views
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse  # For Root API
from rest_framework.views import APIView    # For Root API
from rest_framework.response import Response   # For Root API


from django.contrib.auth.models import User
from .models import Post, Category
from . serializers import CategorySerializer, PostSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly # Making custom permissions



# API using class-based views
# class PostList(APIView):
#     """
#     List all snippets, or create a new Post.
#     """
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostDetail(APIView):
#     """
#     Retrieve, update or delete a Post instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






class PostList(generics.ListCreateAPIView):
    # for adding loggedin user who create post

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
#     perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
#     perform_update(self, serializer) - Called by UpdateModelMixin when saving an existing object instance.
#     perform_destroy(self, instance) - Called by DestroyModelMixin when deleting an object instance.

    queryset = Post.objects.all()
    
#     def get_queryset(self):
#         """Returns Polls that belong to the current user"""
#         return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
    
    serializer_class = PostSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                   IsOwnerOrReadOnly]







# for user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
    })
