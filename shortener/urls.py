from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('shorten/', views.index, name='index'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]
