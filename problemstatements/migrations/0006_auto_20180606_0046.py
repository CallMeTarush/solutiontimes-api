# Generated by Django 2.0.5 on 2018-06-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemstatements', '0005_auto_20180605_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemstatement',
            name='is_long',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='is_medium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='is_short',
            field=models.BooleanField(default=False),
        ),
    ]
