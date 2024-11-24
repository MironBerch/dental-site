# Generated by Django 5.1.2 on 2024-11-02 00:03

import django_ckeditor_5.fields

from django.db import migrations, models

import clinic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='о клинике')),
            ],
            options={
                'verbose_name': 'О клинике',
                'verbose_name_plural': 'О клинике',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное наименование')),
                ('abbreviated_name', models.CharField(max_length=255, verbose_name='Сокращенное наименование')),
                ('INN_KPP', models.CharField(max_length=255, verbose_name='ИНН/КПП')),
                ('OGRN', models.CharField(max_length=255, verbose_name='ОГРН')),
                ('legal_address', models.CharField(max_length=255, verbose_name='Юридический адрес')),
                ('actual_address', models.CharField(max_length=255, verbose_name='Фактический адрес')),
                ('telephone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('fax', models.CharField(max_length=255, verbose_name='факс')),
                ('email', models.CharField(max_length=255, verbose_name='Электронная почта')),
                ('website', models.CharField(max_length=255, verbose_name='Сайт')),
                ('bank_details', models.CharField(max_length=255, verbose_name='Банковские реквизиты')),
            ],
            options={
                'verbose_name': 'реквизиты',
                'verbose_name_plural': 'реквизиты',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название лицензии')),
                ('image', models.ImageField(blank=True, null=True, upload_to=clinic.models.get_license_image_upload_path, verbose_name='фото документа')),
                ('pdf', models.FileField(blank=True, null=True, upload_to=clinic.models.get_license_pdf_upload_path, verbose_name='pdf файл для просмотра документа')),
                ('published', models.BooleanField(blank=True, default=True, verbose_name='является ли опубликованным')),
            ],
            options={
                'verbose_name': 'лицензия',
                'verbose_name_plural': 'лицензии',
            },
        ),
    ]
