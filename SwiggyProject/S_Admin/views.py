from django.contrib import messages
from django.shortcuts import render, redirect
from S_Admin.forms import *
from S_Admin.models import AdminLoginModel, RestaurantTypeModel, StateModel, CityModel, AreaModel
from restaurant.models import RestaurantModel


def admin_login(request):
    return render(request, 's_admin/admin_login.html')


def admin_home(request):
    try:
        username = request.POST.get("username")
        password = request.POST.get('password')
        AdminLoginModel.objects.get(username=username, password=password)
        request.session["status"] = True
        return redirect('admin_home1')
    except AdminLoginModel.DoesNotExist:
        return render(request, 's_admin/admin_login.html', {"error": "Invalid Credentials"})


def admin_home1(request):
    return render(request, 's_admin/admin_home.html')


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')


def open_state(request):
    return render(request, 's_admin/open_state.html',
                  {'state_form': StateForm(), 'state_list': StateModel.objects.all()})


def save_state(request):
    state_form_object = StateForm(request.POST)
    if state_form_object.is_valid():
        state_form_object.save()
        return redirect('open_state')
    else:
        messages.error(request, 'Data is Not Saved')
        return render(request, 's_admin/open_state.html', {'state_form': state_form_object})


def edit_state(request):
    state_id = request.GET.get('state_id')
    state_name = request.GET.get('state_name')
    state_dictionary = {'state_id': state_id, 'state_name': state_name}
    return render(request, 's_admin/open_state.html',
                  {'edit_state_data': state_dictionary, 'state_list': StateModel.objects.all()})


def update_state(request):
    state_id = request.POST.get('state_id')
    state_name = request.POST.get('state_name')
    StateModel.objects.filter(state_id=state_id).update(state_name=state_name)
    return redirect('open_state')


def delete_state(request):
    state_id = request.GET.get('state_id')
    StateModel.objects.get(state_id=state_id).delete()
    return redirect('open_state')


def open_city(request):
    return render(request, 's_admin/open_city.html', {'city_form': CityForm(), 'city_list': CityModel.objects.all()})


def save_city(request):
    city_form_object = CityForm(request.POST)
    if city_form_object.is_valid():
        city_form_object.save()
        return redirect('open_city')
    else:
        messages.error(request, 'Data is Not Saved')
        return render(request, 's_admin/open_city.html', {'city_form': city_form_object})


def edit_city(request):
    city_id = request.GET.get('city_id')
    city_name = request.GET.get('city_name')
    # state_id = request.GET.get('state_id')'state_id' :state_id,
    state_name = request.GET.get('state_name')
    city_dictionary = {'city_id': city_id, 'city_name': city_name, 'state_name': state_name, }
    return render(request, 's_admin/open_city.html',
                  {'edit_city_data': city_dictionary, 'city_list': CityModel.objects.all()})


def update_city(request):
    city_id = request.POST.get('city_id')
    city_name = request.POST.get('city_name')
    # state_name = request.POST.get('state_name')
    # state_id = request.POST.get('state_id')
    CityModel.objects.filter(city_id=city_id).update(city_name=city_name)

    return redirect('open_city')


def delete_city(request):
    city_id = request.GET.get('city_id')
    CityModel.objects.get(city_id=city_id).delete()
    return redirect('open_city')


def open_area(request):
    return render(request, 's_admin/open_area.html', {'area_form': AreaForm(), 'area_list': AreaModel.objects.all()})


def save_area(request):
    area_form_object = AreaForm(request.POST)
    if area_form_object.is_valid():
        area_form_object.save()
        return redirect('open_area')
    else:
        messages.error(request, 'Data is Not Saved')
        return render(request, 's_admin/open_area.html', {'area_form': area_form_object})


def edit_area(request):
    area_id = request.GET.get('area_id')
    area_name = request.GET.get('area_name')
    city_name = request.GET.get('city_name')
    area_dictionary = {'area_id': area_id, 'area_name': area_name, 'city_name': city_name}
    return render(request, 's_admin/open_area.html',
                  {'edit_area_data': area_dictionary, 'area_list': AreaModel.objects.all()})


def update_area(request):
    area_id = request.POST.get('area_id')
    area_name = request.POST.get('area_name')
    AreaModel.objects.filter(area_id=area_id).update(area_name=area_name)
    return redirect('open_area')


def delete_area(request):
    area_id = request.GET.get('area_id')
    AreaModel.objects.get(area_id=area_id).delete()
    return redirect('open_area')


def open_type(request):
    return render(request, 's_admin/open_type.html', {'restaurant_type_form': RestaurantTypeForm,
                                                      'restaurant_type_list': RestaurantTypeModel.objects.all()})


def save_type(request):
    restaurant_type_form_object = RestaurantTypeForm(request.POST)
    if restaurant_type_form_object.is_valid():
        restaurant_type_form_object.save()
        return redirect('open_type')
    else:
        messages.error(request, 'Data Not Saved')
        return render(request, 's_admin/open_type.html', {'restaurant_type_form': restaurant_type_form_object})


def delete_restaurant_type(request):
    restaurant_id = request.GET.get('restaurant_id')
    RestaurantTypeModel.objects.get(restaurant_type_no=restaurant_id).delete()
    return redirect('open_type')


def edit_restaurant_type(request):
    restaurant_id = request.GET.get('restaurant_id')
    restaurant_type = request.GET.get('restaurant_type')
    dict_variable = {'restaurant_id': restaurant_id, 'restaurant_type': restaurant_type}
    return render(request,'s_admin/open_type.html',{'edit_restaurant_data':dict_variable,'restaurant_type_list': RestaurantTypeModel.objects.all()})


def update_restaurant_type(request):
    restaurant_id = request.POST.get('restaurant_id')
    restaurant_name = request.POST.get('restaurant_name')
    RestaurantTypeModel.objects.filter(restaurant_type_no=restaurant_id).update(restaurant_type_name=restaurant_name)
    return redirect('open_type')


def show_pending_restaurant_list(request):
    pending_rest_list=RestaurantModel.objects.filter(restaurant_status='pending')
    return render(request,'s_admin/pending_restaurant_info.html',{'pending_rest_list':pending_rest_list})


def approved_restaurant_info(request):
    restaurant_id=request.GET.get('restaurant_id')
    RestaurantModel.objects.filter(restaurant_id=restaurant_id).update(restaurant_status='approved')
    return redirect('admin_home1')


def cancelled_restaurant_info(request):
    restaurant_id = request.GET.get('restaurant_id')
    RestaurantModel.objects.filter(restaurant_id=restaurant_id).update(restaurant_status='cancelled')
    return redirect('admin_home1')


def show_approved_restaurant_list(request):
    approved_rest_list = RestaurantModel.objects.filter(restaurant_status='approved')
    return render(request, 's_admin/show_approved_restaurant_list.html', {'approved_rest_list': approved_rest_list})


def show_cancelled_restaurant_list(request):
    cancelled_rest_list = RestaurantModel.objects.filter(restaurant_status='cancelled')
    return render(request, 's_admin/show_cancelled_restaurant_list.html', {'cancelled_rest_list': cancelled_rest_list})

