# Generated by Django 4.1.5 on 2024-04-04 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('str_backend', '0002_category_img_url_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img_url',
            field=models.CharField(default='', max_length=250, null=True),
        ),
    ]