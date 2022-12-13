# Generated by Django 4.1.3 on 2022-12-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_arriendoes_totalpago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('user', models.EmailField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('nombreBanco', models.CharField(max_length=50)),
                ('numTarjeta', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MM', models.CharField(max_length=10)),
                ('YY', models.CharField(max_length=10)),
                ('CCV', models.CharField(max_length=10)),
            ],
        ),
    ]