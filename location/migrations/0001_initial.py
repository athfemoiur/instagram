# Generated by Django 2.2 on 2020-03-05 11:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('points', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='points')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
