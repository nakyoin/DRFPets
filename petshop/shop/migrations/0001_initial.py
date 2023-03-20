# Generated by Django 4.1.7 on 2023-03-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='StatusOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statuspet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Статус',
            },
        ),
        migrations.CreateModel(
            name='TypeOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typepet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, default=None, upload_to='')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categ', to='shop.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statsss', to='shop.statusof')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='types', to='shop.typeof')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]
