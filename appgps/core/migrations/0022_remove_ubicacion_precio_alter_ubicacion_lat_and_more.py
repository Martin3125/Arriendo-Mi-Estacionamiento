# Generated by Django 4.1.3 on 2022-11-12 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_ubicacion_fecha_alter_ubicacion_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacion',
            name='precio',
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='lat',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='lng',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
