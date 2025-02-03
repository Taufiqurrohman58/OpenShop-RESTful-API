# Generated by Django 4.2 on 2025-02-02 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('shop', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=25)),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('picture', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
