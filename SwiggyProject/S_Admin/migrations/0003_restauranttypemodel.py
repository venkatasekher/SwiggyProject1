# Generated by Django 2.1 on 2020-04-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('S_Admin', '0002_auto_20200415_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTypeModel',
            fields=[
                ('restaurant_type_no', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant_type_name', models.CharField(max_length=64)),
            ],
        ),
    ]