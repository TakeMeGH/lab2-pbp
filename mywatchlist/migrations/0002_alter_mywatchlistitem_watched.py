# Generated by Django 4.1 on 2022-09-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]