# Generated by Django 2.0.6 on 2018-08-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AddField(
            model_name='like',
            name='post_pk',
            field=models.IntegerField(null=True),
        ),
    ]
