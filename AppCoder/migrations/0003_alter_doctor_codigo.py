# Generated by Django 4.1.7 on 2023-03-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_medicina_paciente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='codigo',
            field=models.IntegerField(),
        ),
    ]
