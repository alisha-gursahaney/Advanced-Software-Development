# Generated by Django 4.1.7 on 2023-04-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorMe', '0011_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutormeuser',
            name='phone_number',
            field=models.CharField(default='1234567890', max_length=20),
        ),
        migrations.AddField(
            model_name='tutormeuser',
            name='preferred_contact',
            field=models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], default='email', max_length=10),
        ),
    ]
