from S_Admin.models import *
from django import forms


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = AdminLoginModel
        fields = "__all__"


class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ['state_name']


class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_id',)


class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = '__all__'
        exclude = ('area_id',)

class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model=RestaurantTypeModel
        fields=['restaurant_type_name']
