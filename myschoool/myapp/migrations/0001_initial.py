# Generated by Django 5.1.5 on 2025-05-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='courses')),
                ('name', models.CharField(max_length=255)),
                ('fee', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='courses')),
                ('name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
