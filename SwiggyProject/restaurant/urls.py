from django.urls import path

from restaurant import views

urlpatterns = [
    path('',views.restaurant_home,name='restaurant_home'),
    path('register_restaurant',views.register_restaurant,name='register_restaurant'),
    path('save_restaurant',views.save_restaurant,name='save_restaurant'),
]
