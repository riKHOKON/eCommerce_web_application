# Generated by Django 2.0.5 on 2018-05-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180520_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
