from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from . serializers import RegisterSerializer
# Create your views here.
from .models import User, UserProfile, Category, Post

class RegisterView(generics.GenericAPIView):

# {
# "email": "test@gmail.com",
# "username": "shakil2",
# "password": "100%love",
# "category": {
#     "category_name": "Travel"
# },
# "post": {
#     "title": "post title",
#     "description": "post descriptions"
# }
# }

	serializer_class = RegisterSerializer
	def post(self, request):
		user = request.data
		serializer = self.serializer_class(data=user)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		user_data = serializer.data
		return Response(user_data, status=status.HTTP_201_CREATED)

    

class AllDataAPIView(generics.RetrieveUpdateDestroyAPIView):
	# queryset = User.objects.all()
	serializer_class = RegisterSerializer

	# def get_queryset():
	# 	pass

		


