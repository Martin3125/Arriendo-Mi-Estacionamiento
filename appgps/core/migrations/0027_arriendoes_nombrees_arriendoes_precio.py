# Generated by Django 4.0.4 on 2022-11-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_arriendoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='arriendoes',
            name='nombreEs',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='arriendoes',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
