# Generated by Django 3.2.13 on 2022-05-22 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faceRecognition', '0009_auto_20220522_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('course_image', models.ImageField(upload_to='course_image/')),
            ],
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceRecognition.courses'),
        ),
        migrations.AlterField(
            model_name='studentattendancehistory',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceRecognition.courses'),
        ),
    ]
