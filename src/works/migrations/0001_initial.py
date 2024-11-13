# Generated by Django 5.1.2 on 2024-11-02 14:47

import django.db.models.deletion
import django_ckeditor_5.fields
import works.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('information', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='информация')),
                ('published', models.BooleanField(blank=True, default=True, verbose_name='является ли опубликованным')),
            ],
            options={
                'verbose_name': 'работа',
                'verbose_name_plural': 'работы',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=works.models.get_staff_image_upload_path)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='works.work')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фото',
            },
        ),
    ]