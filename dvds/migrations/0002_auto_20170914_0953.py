# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='typeOf',
        ),
        migrations.AddField(
            model_name='dvd',
            name='type_of',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dvds.Type_of'),
            preserve_default=False,
        ),
    ]
