# Generated by Django 5.0.6 on 2024-06-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_mobilenumber_otp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MobileNumber',
        ),
        migrations.RenameField(
            model_name='otp',
            old_name='box1',
            new_name='otp_number',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='box2',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='box3',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='box4',
        ),
        migrations.AddField(
            model_name='otp',
            name='phone',
            field=models.CharField(default='54545', max_length=10),
            preserve_default=False,
        ),
    ]
