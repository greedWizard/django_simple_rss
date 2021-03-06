# Generated by Django 3.2.5 on 2021-07-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSSFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('rss_url', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RSSFeedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('url', models.URLField(unique=True)),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
