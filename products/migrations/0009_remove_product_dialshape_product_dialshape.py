# Generated by Django 5.0.6 on 2024-06-28 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_dialshape_product_dialshape'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dialshape',
        ),
        migrations.AddField(
            model_name='product',
            name='dialshape',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.dialshape'),
        ),
    ]
