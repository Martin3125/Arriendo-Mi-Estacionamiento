# Generated by Django 4.1.3 on 2022-12-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendoes',
            name='h_inicio',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='arriendoes',
            name='h_salida',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
