from django.db import models
from S_Admin.models import AreaModel, RestaurantTypeModel


class RestaurantModel(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=64)
    restaurant_contact = models.IntegerField()
    restaurant_email = models.EmailField()
    restaurant_area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    restaurant_type=models.ForeignKey(RestaurantTypeModel,on_delete=models.CASCADE)
    restaurant_password=models.CharField(max_length=64)
    restaurant_otp=models.IntegerField()
    restaurant_status=models.CharField(max_length=32)
