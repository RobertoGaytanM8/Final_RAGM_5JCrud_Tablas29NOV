# Generated by Django 5.1.2 on 2024-11-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptantes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptante',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
