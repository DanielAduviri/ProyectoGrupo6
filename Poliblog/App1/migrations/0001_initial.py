# Generated by Django 4.0.1 on 2022-01-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
