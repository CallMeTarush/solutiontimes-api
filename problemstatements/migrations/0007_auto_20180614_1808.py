# Generated by Django 2.0.5 on 2018-06-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemstatements', '0006_auto_20180606_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='no_of_mentors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='no_of_sponsors',
            field=models.IntegerField(default=0),
        ),
    ]
