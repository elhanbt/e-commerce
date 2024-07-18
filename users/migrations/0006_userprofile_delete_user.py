# Generated by Django 5.0.6 on 2024-07-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_created_on_user_isdelete'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('fname', models.CharField(max_length=200, verbose_name='First Name')),
                ('lname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userprofile_userprofile',
                'ordering': ('fname',),
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]