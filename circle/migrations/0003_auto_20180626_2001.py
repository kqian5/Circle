# Generated by Django 2.0.6 on 2018-06-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]