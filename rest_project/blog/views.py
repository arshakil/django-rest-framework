from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from . serializers import RegisterSerializer, UserListSerializer, UserProfileSerializer
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
	queryset = User.objects.all()
	serializer_class = RegisterSerializer

# 	# def get_queryset():
# 	# 	pass

		


class UserList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserProfile(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# continent
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from .models import Continent, Region
from .serializers import ContinentListSerializer, RegionSerializer, RegionNewSerializer


class ContinentCreateAPIView(CreateAPIView):
    serializer_class = ContinentListSerializer
    queryset = Continent.objects.all()


class ContinentListAPIView(ListAPIView):
    serializer_class = ContinentListSerializer
    queryset = Continent.objects.all()
    permission_classes = [AllowAny]
    # permission for all because it is necessary for register an organization


class ContinentUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ContinentListSerializer
    queryset = Continent.objects.all()


class ContinentDeleteAPIView(DestroyAPIView):
    serializer_class = ContinentListSerializer
    queryset = Continent.objects.all()

# Region
# for deropdown froeign key
class RegionNewAPIView(CreateAPIView):
    serializer_class = RegionNewSerializer
    queryset = Region.objects.all()

class RegionCreateAPIView(CreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionListAPIView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = [AllowAny]
    # permission for all because it is necessary for register an organization


class RegionUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionDeleteAPIView(DestroyAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
