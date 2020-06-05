# Generated by Django 3.0.6 on 2020-06-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
                ('image', models.ImageField(upload_to='images/')),
                ('information', models.TextField(max_length=300)),
            ],
        ),
    ]
