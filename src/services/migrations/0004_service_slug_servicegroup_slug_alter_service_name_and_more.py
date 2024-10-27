# Generated by Django 5.1.2 on 2024-10-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicegroup_remove_service_tag_service_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='servicegroup',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='название'),
        ),
    ]