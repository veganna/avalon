# Generated by Django 3.2.14 on 2022-07-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20220708_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='nftTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
