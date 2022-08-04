# Generated by Django 3.2.14 on 2022-07-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='faqCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faqName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='nftCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftCategoryName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='nftCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftCoinName', models.CharField(max_length=25)),
                ('nftConvertValue', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='nftTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftTagName', models.CharField(max_length=25)),
                ('nftTagColor', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='nftUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='roadMapSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='roadMapModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarterTitle', models.CharField(max_length=20)),
                ('quarterList', models.ManyToManyField(to='mainsite.roadMapSteps')),
            ],
        ),
        migrations.CreateModel(
            name='nftItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nftTitle', models.CharField(max_length=255)),
                ('nftPrice', models.FloatField(default=0)),
                ('nftPhoto', models.ImageField(blank=True, upload_to='')),
                ('nftLikes', models.IntegerField(default=0)),
                ('nftCategories', models.ManyToManyField(to='mainsite.nftCategory')),
                ('nftCoins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.nftcoin')),
                ('nftCreators', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.nftusers')),
            ],
        ),
        migrations.CreateModel(
            name='faqItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faqTitle', models.CharField(max_length=255)),
                ('faqText', models.TextField()),
                ('faqCategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.faqcategories')),
            ],
        ),
        migrations.CreateModel(
            name='contactMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameField', models.CharField(max_length=255)),
                ('mailField', models.EmailField(max_length=255)),
                ('messageField', models.TextField()),
                ('dateField', models.DateTimeField(auto_now=True)),
                ('subjectField', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.contactsubjects')),
            ],
        ),
    ]