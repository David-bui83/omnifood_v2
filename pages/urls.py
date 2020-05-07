from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('message', views.message, name="message"),
  path('email', views.email, name="email"),
]