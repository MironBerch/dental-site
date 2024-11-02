# Generated by Django 5.1.2 on 2024-11-02 00:03

import django_ckeditor_5.fields
import staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name': 'роль или специализация',
                'verbose_name_plural': 'роли или специализации',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=staff.models.get_staff_image_upload_path, verbose_name='фото работника')),
                ('fio', models.CharField(max_length=100, unique=True, verbose_name='ФИО')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('information', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='информация')),
                ('stage', models.CharField(blank=True, choices=[('Руководитель', 'Руководитель'), ('Администратор', 'Администратор'), ('Мед персонал', 'Мед персонал'), ('Младщий мед персонал', 'Младщий мед персонал')], max_length=50, verbose_name='позиция')),
                ('published', models.BooleanField(blank=True, default=True, verbose_name='является ли опубликованным')),
                ('roles', models.ManyToManyField(blank=True, to='staff.role', verbose_name='роли или специализации')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
            },
        ),
    ]
