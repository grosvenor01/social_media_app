# Generated by Django 4.0.6 on 2022-07-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0003_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('followers', models.IntegerField()),
            ],
        ),
    ]
