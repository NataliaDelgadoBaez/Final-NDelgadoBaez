# Generated by Django 4.2 on 2023-10-19 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Tienda_app.disco')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]