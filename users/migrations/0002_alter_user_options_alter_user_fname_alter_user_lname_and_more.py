# Generated by Django 5.0.6 on 2024-06-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('fname',)},
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=200, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=200, verbose_name='Last Name'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_users',
        ),
    ]