# Generated by Django 4.0.6 on 2022-07-06 12:48

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nbr_like', models.IntegerField(default=0)),
                ('user', models.CharField(max_length=150)),
                ('caption', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='posts')),
            ],
        ),
    ]
