# Generated by Django 4.1.3 on 2022-11-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='precio',
            field=models.IntegerField(default=7),
        ),
    ]
