# Generated by Django 2.2.2 on 2019-06-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0013_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='summoner',
            name='full_import_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]