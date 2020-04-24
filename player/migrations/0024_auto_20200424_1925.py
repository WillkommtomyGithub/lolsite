# Generated by Django 2.2.2 on 2020-04-24 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0023_summonerlink_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ign', models.CharField(blank=True, db_index=True, default='', max_length=256, unique=True)),
                ('position', models.CharField(blank=True, choices=[('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('adc', 'adc'), ('sup', 'sup')], db_index=True, default='', max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='summoner',
            name='pro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.Pro'),
        ),
    ]