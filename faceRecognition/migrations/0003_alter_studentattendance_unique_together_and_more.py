# Generated by Django 4.0.4 on 2022-05-22 03:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faceRecognition', '0002_studentattendance_course'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentattendance',
            unique_together={('user', 'time')},
        ),
        migrations.RemoveField(
            model_name='studentattendance',
            name='standard',
        ),
    ]
