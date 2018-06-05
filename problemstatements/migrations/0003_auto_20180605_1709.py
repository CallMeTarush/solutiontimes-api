# Generated by Django 2.0.5 on 2018-06-05 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problemstatements', '0002_auto_20180524_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemstatement',
            name='contestants',
            field=models.ManyToManyField(related_name='_problemstatement_contestants_+', through='problemstatements.Solution', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='mentors',
            field=models.ManyToManyField(related_name='_problemstatement_mentors_+', through='problemstatements.Mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='sponsors',
            field=models.ManyToManyField(related_name='_problemstatement_sponsors_+', through='problemstatements.Sponsor', to=settings.AUTH_USER_MODEL),
        ),
    ]