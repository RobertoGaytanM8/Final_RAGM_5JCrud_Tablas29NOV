# Generated by Django 5.1.2 on 2024-11-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('edad', models.PositiveSmallIntegerField()),
                ('sexo', models.CharField(max_length=15)),
            ],
        ),
    ]
