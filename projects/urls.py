from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('dice/', views.shop, name='shop_page'),
    path('dice/<int:pk>/', views.dice_page, name='dice_page'),
    path('about/', views.about_page, name="about")
]