# Generated by Django 5.0.6 on 2024-07-01 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_feature_product_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
    ]
