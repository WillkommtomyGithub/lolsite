# Generated by Django 2.1.5 on 2019-02-07 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20190206_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='FromItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IntoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(db_index=True)),
                ('version', models.CharField(blank=True, db_index=True, default='', max_length=128)),
                ('language', models.CharField(blank=True, db_index=True, default='en_US', max_length=32)),
                ('colloq', models.CharField(blank=True, default='', max_length=256)),
                ('depth', models.IntegerField()),
                ('group', models.CharField(blank=True, default='', max_length=128)),
                ('description', models.CharField(blank=True, default='', max_length=2048)),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('plaintext', models.CharField(blank=True, default='', max_length=256)),
                ('required_ally', models.CharField(blank=True, default='', max_length=256)),
                ('required_champion', models.CharField(blank=True, default='', max_length=256)),
                ('in_store', models.BooleanField(default=True)),
                ('consumed', models.BooleanField(default=False)),
                ('consume_on_full', models.BooleanField(default=False)),
                ('special_recipe', models.IntegerField(blank=True, null=True)),
                ('stacks', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=256)),
                ('value', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='effects', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemGold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.IntegerField()),
                ('purchasable', models.BooleanField(default=False)),
                ('sell', models.IntegerField()),
                ('total', models.IntegerField()),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gold', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(blank=True, default='', max_length=128)),
                ('group', models.CharField(max_length=128)),
                ('h', models.IntegerField()),
                ('sprite', models.CharField(max_length=128)),
                ('w', models.IntegerField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('value', models.BooleanField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rune', models.BooleanField(default=False)),
                ('tier', models.IntegerField()),
                ('_type', models.CharField(blank=True, default='', max_length=128)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rune', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=128)),
                ('value', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='data.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, unique=True)),
                ('items', models.ManyToManyField(related_name='tags', to='data.Item')),
            ],
        ),
        migrations.AddField(
            model_name='intoitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intoitems', to='data.Item'),
        ),
        migrations.AddField(
            model_name='fromitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromitems', to='data.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='itemstat',
            unique_together={('item', 'key')},
        ),
        migrations.AlterUniqueTogether(
            name='itemmap',
            unique_together={('item', 'key')},
        ),
        migrations.AlterUniqueTogether(
            name='itemeffect',
            unique_together={('item', 'key')},
        ),
    ]
