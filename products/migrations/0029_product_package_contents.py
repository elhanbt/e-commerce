# Generated by Django 5.0.6 on 2024-07-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_product_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='package_contents',
            field=models.TextField(blank=True, null=True),
        ),
    ]