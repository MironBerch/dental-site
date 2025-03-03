# Generated by Django 5.1.2 on 2024-12-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='opening_hours',
            field=models.CharField(blank=True, max_length=255, verbose_name='Часы работы'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_numbers',
            field=models.CharField(blank=True, max_length=255, verbose_name='Номера телефонов'),
        ),
    ]
