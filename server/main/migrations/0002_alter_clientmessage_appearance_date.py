# Generated by Django 4.0.1 on 2022-02-06 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmessage',
            name='appearance_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата отправки'),
        ),
    ]
