# Generated by Django 4.1.7 on 2023-03-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorMe', '0005_rename_descr_course_course_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorclasses',
            name='number',
            field=models.CharField(default='', max_length=255),
        ),
    ]
