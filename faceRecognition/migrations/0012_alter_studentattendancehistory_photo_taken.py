# Generated by Django 3.2.13 on 2022-05-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceRecognition', '0011_auto_20220522_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendancehistory',
            name='photo_taken',
            field=models.CharField(max_length=255, null=True),
        ),
    ]