# Generated by Django 4.1.7 on 2023-03-02 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
