# Generated by Django 4.1.7 on 2023-03-02 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automaint', '0002_alter_car_image_alter_car_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maint',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Maintenance', to='automaint.car'),
        ),
    ]