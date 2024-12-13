# Generated by Django 5.1.4 on 2024-12-12 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosetInfo',
            fields=[
                ('closet_id', models.AutoField(primary_key=True, serialize=False)),
                ('closet_name', models.CharField(max_length=255)),
                ('closet_type', models.CharField(max_length=255)),
                ('closet_location', models.CharField(max_length=255)),
                ('closet_size', models.CharField(max_length=255)),
                ('closet_color', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'closet_info',
                'unique_together': {('user', 'closet_id')},
            },
        ),
        migrations.CreateModel(
            name='ClothingItem',
            fields=[
                ('clothing_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('clothing_item_name', models.CharField(max_length=255)),
                ('clothing_item_file_path', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'clothing_item',
                'unique_together': {('user', 'clothing_item_id')},
            },
        ),
        migrations.CreateModel(
            name='ClosetStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hanger_number', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('closet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.closetinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('clothing_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.clothingitem')),
            ],
            options={
                'db_table': 'closet_status',
                'unique_together': {('user', 'closet', 'hanger_number', 'clothing_item')},
            },
        ),
        migrations.CreateModel(
            name='OutfitInfo',
            fields=[
                ('outfit_id', models.AutoField(primary_key=True, serialize=False)),
                ('outfit_name', models.CharField(max_length=255)),
                ('clothing_items', models.ManyToManyField(to='database.clothingitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'outfit_info',
                'unique_together': {('user', 'outfit_id')},
            },
        ),
    ]
