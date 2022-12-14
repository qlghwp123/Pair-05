from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path("<int:user_pk>/", views.detail, name='detail'),
    path("login/", views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),

]
