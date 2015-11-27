# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0003_auto_20151126_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='descrizione_interna',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
    ]
