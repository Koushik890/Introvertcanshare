# Generated by Django 2.2.1 on 2020-01-19 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200119_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ngo_name',
        ),
    ]
