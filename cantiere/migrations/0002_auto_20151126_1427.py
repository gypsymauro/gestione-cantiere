# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervento',
            old_name='data_inizio',
            new_name='datainizio',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='data_riapertura',
            new_name='datariapertura',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='data_sospensione',
            new_name='datasospensione',
        ),
        migrations.AddField(
            model_name='intervento',
            name='datachiusura',
            field=models.DateTimeField(null=True, verbose_name=b'Data di chiusura', blank=True),
        ),
    ]
