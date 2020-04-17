from django.db import models
from django import forms


class AdminLoginModel(models.Model):
    username = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=32)
    otp = models.IntegerField()


class StateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.state_name


class CityModel(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=32)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class AreaModel(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=32)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name


class RestaurantTypeModel(models.Model):
    restaurant_type_no = models.AutoField(primary_key=True)
    restaurant_type_name = models.CharField(max_length=64)

    def __str__(self):
        return self.restaurant_type_name

