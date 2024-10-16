# Generated by Django 5.1.1 on 2024-10-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'apartment', 'verbose_name_plural': 'apartments'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'house', 'verbose_name_plural': 'houses'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
