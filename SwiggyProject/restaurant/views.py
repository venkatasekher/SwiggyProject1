from django.shortcuts import render, redirect
from restaurant.forms import *
from django.contrib import messages


def restaurant_home(request):
    return render(request, 'restaurant/restaurant_home.html')


def register_restaurant(request):
    return render(request, 'restaurant/restaurant_registration.html',
                  {'restaurant_reg_form': RestaurantForm(), 'restaurant_list': RestaurantModel.objects.all()})


def save_restaurant(request):
    restaurant_form_object=RestaurantForm(request.POST)
    if restaurant_form_object.is_valid():
        db=restaurant_form_object.save(commit=False)
        db.restaurant_otp=1234
        db.restaurant_status='pending'
        restaurant_form_object.save()
        messages.success(request,"Once admin approve your registration, You will receive Email and Text Message ")
        return redirect('restaurant_home')
    else:
        return render(request,'restaurant/restaurant_registration.html',{'restaurant_form_object':restaurant_form_object})