# Generated by Django 4.1 on 2022-10-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0030_alter_userswatchlist_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userswatchlist',
            name='watchlist',
            field=models.ManyToManyField(blank=True, to='watchlist.watchlist'),
        ),
    ]
