# Generated by Django 4.0.4 on 2022-05-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceRecognition', '0004_studentattendancehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
