# Generated by Django 2.2.2 on 2020-06-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images\\'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images\\'),
        ),
    ]
