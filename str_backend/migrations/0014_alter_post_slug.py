# Generated by Django 5.0.4 on 2024-04-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('str_backend', '0013_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]