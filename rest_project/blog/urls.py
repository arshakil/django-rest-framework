from django.urls import path
from .views import RegisterView, AllDataAPIView, UserList, UserProfile

# continent and region
from django.conf.urls import url
from .views import ContinentCreateAPIView, ContinentListAPIView, ContinentUpdateAPIView
from .views import RegionCreateAPIView,RegionListAPIView,RegionUpdateAPIView, RegionNewAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('user/<int:pk>/', UserList.as_view(), name="posts"),
    path('profile/<int:pk>/', UserProfile.as_view(), name="profile"),
    path('register/<int:pk>/', AllDataAPIView.as_view(), name='single-user'),

    # continent
	url(r'^continent/$', ContinentListAPIView.as_view()),
	url(r'^continent/new/$', ContinentCreateAPIView.as_view()),
	url(r'^continent/(?P<pk>\d+)/edit/$', ContinentUpdateAPIView.as_view()),
	# region
	url(r'^region_new/$', RegionNewAPIView.as_view()),
	url(r'^region/$', RegionListAPIView.as_view()),
	url(r'^region/new/$', RegionCreateAPIView.as_view()),
	url(r'^region/(?P<pk>\d+)/edit/$', RegionUpdateAPIView.as_view()),

]