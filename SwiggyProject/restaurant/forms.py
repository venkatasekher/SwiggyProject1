from django import forms
from restaurant.models import *


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = RestaurantModel
        fields = '__all__'
        exclude = ('restaurant_id','restaurant_otp','restaurant_status')
