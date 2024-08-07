from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten/', views.shortener, name='index'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
