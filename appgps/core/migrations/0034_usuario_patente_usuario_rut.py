# Generated by Django 4.1.3 on 2022-12-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_arriendoes_h_inicio_alter_arriendoes_h_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='patente',
            field=models.CharField(default=0, max_length=8),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
