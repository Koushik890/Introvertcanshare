# Generated by Django 2.2.1 on 2020-01-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200118_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='organisation_name',
            field=models.TextField(blank=True),
        ),
    ]
