# Generated by Django 4.2.4 on 2023-08-25 10:09

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=12, validators=[app.models.phone_validate], verbose_name='Телефон'),
        ),
    ]
