# Generated by Django 2.1.2 on 2021-06-16 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'サンプル1', 'verbose_name_plural': 'サンプル2'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_7',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_9',
        ),
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(default=datetime.date(2021, 6, 16), verbose_name='日付'),
        ),
        migrations.AddField(
            model_name='item',
            name='money',
            field=models.IntegerField(default=0, verbose_name='金額'),
        ),
        migrations.AddField(
            model_name='item',
            name='other',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='備考'),
        ),
    ]
