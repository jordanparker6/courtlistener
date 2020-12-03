# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-18 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0096_add_court_fields_and_noops'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='html_anon_2020',
            field=models.TextField(blank=True, help_text='HTML of 2020 anonymous archive'),
        ),
        migrations.AlterField(
            model_name='docket',
            name='source',
            field=models.SmallIntegerField(choices=[(0, 'Default'), (1, 'RECAP'), (2, 'Scraper'), (3, 'RECAP and Scraper'), (4, 'Columbia'), (6, 'Columbia and Scraper'), (5, 'Columbia and RECAP'), (7, 'Columbia, RECAP, and Scraper'), (8, 'Integrated Database'), (9, 'RECAP and IDB'), (10, 'Scraper and IDB'), (11, 'RECAP, Scraper, and IDB'), (12, 'Columbia and IDB'), (13, 'Columbia, RECAP, and IDB'), (14, 'Columbia, Scraper, and IDB'), (15, 'Columbia, RECAP, Scraper, and IDB'), (16, 'Harvard'), (17, 'Scraper and Harvard'), (32, 'Direct court input'), (64, '2020 anonymous database'), (66, '2020 anonymous database and Scraper'), (80, '2020 anonymous database and Harvard'), (82, '2020 anonymous database, Scraper, and Harvard')], help_text='contains the source of the Docket.'),
        ),
    ]