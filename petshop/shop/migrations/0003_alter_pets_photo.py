# Generated by Django 4.1.7 on 2023-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_pets_status_alter_pets_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='photo',
            field=models.URLField(blank=True, default=None),
        ),
    ]
