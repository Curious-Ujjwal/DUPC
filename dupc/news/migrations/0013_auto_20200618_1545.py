# Generated by Django 3.0.6 on 2020-06-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200618_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='has_file',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='has_url',
            field=models.BooleanField(default=True),
        ),
    ]
