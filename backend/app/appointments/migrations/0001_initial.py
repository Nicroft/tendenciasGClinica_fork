# Generated by Django 5.1.1 on 2024-09-22 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y hora')),
                ('motivo_consulta', models.TextField(verbose_name='Motivo de la consulta')),
                ('estado', models.CharField(default='Programada', editable=False, max_length=20)),
            ],
        ),
    ]
