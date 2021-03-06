# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-26 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Banner Name')),
                ('title', models.CharField(max_length=100, verbose_name='Banner Title')),
                ('main_copy', models.TextField(max_length=200, verbose_name='Main Copy')),
                ('button_copy', models.CharField(max_length=50, verbose_name='Button Copy')),
                ('theme', models.CharField(choices=[(b'default', b'Default'), (b'gradient', b'Gradient'), (b'dinohead', b'Dinohead')], default=b'default', max_length=20, verbose_name='Theme')),
                ('active', models.BooleanField(verbose_name='Activate')),
                ('priority', models.PositiveSmallIntegerField(default=100, verbose_name='Priority (1-100)')),
            ],
        ),
    ]
