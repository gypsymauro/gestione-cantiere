# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0002_auto_20151126_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervento',
            old_name='datachiusura',
            new_name='data_chiusura',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='datainizio',
            new_name='data_inizio',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='datariapertura',
            new_name='data_riapertura',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='datasospensione',
            new_name='data_sospensione',
        ),
    ]
