# Generated by Django 4.2 on 2023-10-18 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disco',
            old_name='artista',
            new_name='autor',
        ),
        migrations.RemoveField(
            model_name='disco',
            name='precio',
        ),
    ]
