# Generated by Django 4.1.7 on 2023-03-20 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_doctor_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='publisher',
        ),
    ]
