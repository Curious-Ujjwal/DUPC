# Generated by Django 3.0.8 on 2020-07-25 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
    ]
