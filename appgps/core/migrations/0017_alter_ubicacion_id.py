# Generated by Django 4.1.3 on 2022-11-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_ubicacion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]