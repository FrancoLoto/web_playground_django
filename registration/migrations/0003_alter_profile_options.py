# Generated by Django 4.0.6 on 2022-08-08 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__username']},
        ),
    ]
