# Generated by Django 4.1.7 on 2023-03-20 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stat', to='shop.statusof'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='shop.typeof'),
        ),
    ]
