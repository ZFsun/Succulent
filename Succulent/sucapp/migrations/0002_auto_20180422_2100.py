# Generated by Django 2.0.2 on 2018-04-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucinfo',
            name='introduction',
            field=models.TextField(max_length=1000),
        ),
    ]