# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0006_auto_20151127_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costo',
            name='al',
            field=models.DateTimeField(null=True, verbose_name=b'Valido al', blank=True),
        ),
    ]
