# Generated by Django 5.0.6 on 2024-07-02 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_product_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
    ]
