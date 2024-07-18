# Generated by Django 5.0.6 on 2024-07-05 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_remove_userwishlist_userprofile'),
        ('users', '0009_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userwishlist',
            options={'ordering': ('userprofile',)},
        ),
        migrations.AddField(
            model_name='userwishlist',
            name='userprofile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]