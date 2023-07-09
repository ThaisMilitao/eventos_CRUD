from django.urls import path
from . import views

# caminho de cada funçao
urlpatterns = [
  path('login', views.login, name = 'login'),
  path('signUp', views.signUp, name = 'signUp'),
  path('logOut', views.logOut, name = 'logOut'),


]