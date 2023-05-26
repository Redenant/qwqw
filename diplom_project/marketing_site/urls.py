from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='marketing_site/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='marketing_site/logout.html'), name='logout'),
    path('privacy/', privacy, name='privacy'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('my_orders/', my_orders, name='my_orders'),
]
