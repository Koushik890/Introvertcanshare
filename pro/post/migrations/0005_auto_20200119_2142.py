# Generated by Django 2.2.1 on 2020-01-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200119_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='organisation_name',
        ),
        migrations.AddField(
            model_name='post',
            name='ngo_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]