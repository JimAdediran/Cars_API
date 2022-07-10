# Generated by Django 4.0.5 on 2022-07-10 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0002_car_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealerships'),
            preserve_default=False,
        ),
    ]
