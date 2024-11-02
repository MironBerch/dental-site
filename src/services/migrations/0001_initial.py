# Generated by Django 5.1.2 on 2024-11-02 00:03

import django.db.models.deletion
import django_ckeditor_5.fields
import services.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('information', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='информация')),
                ('image', models.ImageField(blank=True, null=True, upload_to=services.models.get_license_image_upload_path, verbose_name='фото документа')),
                ('published', models.BooleanField(blank=True, default=True, verbose_name='является ли опубликованным')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.servicegroup', verbose_name='группа')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
    ]
