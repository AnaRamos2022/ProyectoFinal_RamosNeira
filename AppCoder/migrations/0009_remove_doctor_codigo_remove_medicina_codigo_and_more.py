# Generated by Django 4.1.7 on 2023-03-23 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_remove_doctor_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='medicina',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='codigo',
        ),
    ]
