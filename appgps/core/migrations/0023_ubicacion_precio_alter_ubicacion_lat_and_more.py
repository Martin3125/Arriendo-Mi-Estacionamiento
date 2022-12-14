# Generated by Django 4.1.3 on 2022-11-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_ubicacion_precio_alter_ubicacion_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='user',
            field=models.EmailField(max_length=50),
        ),
    ]
