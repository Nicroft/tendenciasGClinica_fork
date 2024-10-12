# Generated by Django 5.1.1 on 2024-09-29 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto')),
                ('detalles', models.TextField(blank=True, verbose_name='Detalles')),
                ('estado_pago', models.CharField(default='Pendiente', max_length=20)),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Paciente')),
            ],
        ),
    ]