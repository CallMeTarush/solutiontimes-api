# Generated by Django 2.0.4 on 2018-05-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemstatements', '0005_auto_20180509_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemstatement',
            name='video_id',
            field=models.TextField(default='8tPnX7OPo0Q'),
        ),
        migrations.AlterField(
            model_name='problemstatement',
            name='submissions',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='problemstatement',
            name='videolink',
            field=models.CharField(max_length=100),
        ),
    ]