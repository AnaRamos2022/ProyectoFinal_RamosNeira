# Generated by Django 4.1.7 on 2023-03-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_remove_doctor_codigo_remove_medicina_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicina',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='medicinas'),
        ),
    ]