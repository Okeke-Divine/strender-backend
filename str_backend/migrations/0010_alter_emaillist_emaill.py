# Generated by Django 4.1.5 on 2024-04-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('str_backend', '0009_emaillist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillist',
            name='emaill',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
