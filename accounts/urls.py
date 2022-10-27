from django import views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, nmae='signup'),
    path('', views.index, name='index'),
    path("<int:user_pk>/", views.detail, nmae='detail'),
    path("login/", views.login, name='login'),
    

]
