from django.urls import path
from .views import RegisterView, AllDataAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('register/<int:pk>/', AllDataAPIView.as_view(), name='single-user'),

]