# Generated by Django 3.2.13 on 2022-06-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticmanager', '0002_staticmanager_linkobj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticmanager',
            name='linkobj',
        ),
        migrations.AddField(
            model_name='staticmanager',
            name='linkobjb',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='staticmanager',
            name='linkobjh',
            field=models.CharField(default='', max_length=255),
        ),
    ]
