# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allegato',
            options={'verbose_name': 'Allegato', 'verbose_name_plural': 'File Allegati'},
        ),
    ]
