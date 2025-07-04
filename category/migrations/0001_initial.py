# Generated by Django 5.2.3 on 2025-07-04 07:29

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('cat_img', models.ImageField(blank=True, null=True, upload_to=category.models._upload_to)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
