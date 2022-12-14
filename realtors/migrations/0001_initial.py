# Generated by Django 4.1 on 2022-08-15 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Realter Name')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Details')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Num')),
                ('email', models.CharField(max_length=50, verbose_name='Realter Email')),
                ('top_seller', models.BooleanField(default=False, verbose_name='Top Seller Status')),
                ('date_hired', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Hired Date')),
            ],
        ),
    ]
