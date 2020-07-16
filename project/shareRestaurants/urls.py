from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail', views.restaurant_detail),
    path('restaurantCreate/', views.restaurant_create),
    path('categoryCreate/', views.category_create)
]
