# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0005_auto_20151127_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allegato',
            options={'verbose_name': 'Allegato', 'verbose_name_plural': 'Allegati'},
        ),
        migrations.AlterModelOptions(
            name='centrocosto',
            options={'verbose_name': 'Centro di costo', 'verbose_name_plural': 'Centri di costo'},
        ),
        migrations.AlterModelOptions(
            name='costo',
            options={'verbose_name': 'Tipo di costo', 'verbose_name_plural': 'Tipo di costo'},
        ),
        migrations.AlterModelOptions(
            name='interventorisorsa',
            options={'verbose_name': 'Risorsa x intervento', 'verbose_name_plural': 'Risorse usate'},
        ),
        migrations.AlterModelOptions(
            name='risorsa',
            options={'verbose_name': 'Risorsa', 'verbose_name_plural': 'Risorse'},
        ),
        migrations.AlterModelOptions(
            name='segnalazione',
            options={'verbose_name': 'Segnalazione', 'verbose_name_plural': 'Segnalazioni'},
        ),
        migrations.AlterModelOptions(
            name='squadra',
            options={'verbose_name': 'Squadra', 'verbose_name_plural': 'Squadre'},
        ),
        migrations.AlterModelOptions(
            name='statointervento',
            options={'verbose_name': 'Stato intervento', 'verbose_name_plural': 'Stati degli interventi'},
        ),
        migrations.AlterModelOptions(
            name='statosegnalazione',
            options={'verbose_name': 'Stato della segnalazione', 'verbose_name_plural': 'Stati della segnalazione'},
        ),
        migrations.AddField(
            model_name='intervento',
            name='beneficiario',
            field=models.CharField(default=b'', max_length=300, blank=True),
        ),
    ]
