# Generated by Django 4.1 on 2022-09-03 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0009_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_by',
        ),
    ]
