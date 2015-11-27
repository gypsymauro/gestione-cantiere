# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantiere', '0004_intervento_descrizione_interna'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intervento',
            options={'verbose_name': 'Intervento', 'verbose_name_plural': 'Interventi'},
        ),
        migrations.RenameField(
            model_name='allegato',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='centrocosto',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='costo',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='intervento',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='interventorisorsa',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='risorsa',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='segnalazione',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='squadra',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='statointervento',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='statosegnalazione',
            old_name='cancellato',
            new_name='deleted',
        ),
        migrations.AlterField(
            model_name='allegato',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allegato',
            name='descrizione',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='allegato',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allegato',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='allegato',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='descrizione',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='nome',
            field=models.CharField(default=b'', max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='al',
            field=models.DateTimeField(verbose_name=b'Valido al', blank=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='dal',
            field=models.DateTimeField(verbose_name=b'Valido dal', blank=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='costo',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='buoni',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='descrizione',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='descrizione_interna',
            field=models.TextField(default=b'', max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='oggetto',
            field=models.CharField(default=b'', max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='spese',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='interventorisorsa',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='interventorisorsa',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='interventorisorsa',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='codice_protocollo',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='targa',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='risorsa',
            name='tipo',
            field=models.CharField(default=b'persona', max_length=300, choices=[(b'persona', b'Persona'), (b'mezzo', b'Mezzo'), (b'attrezzatura', b'Attrezzatura'), (b'ditta', b'Ditta'), (b'altro', b'Altro')]),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='descrizione',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='descrizione_interna',
            field=models.TextField(max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='oggetto',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='segnalazione',
            name='segnalatore',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='statointervento',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statointervento',
            name='descrizione',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='statointervento',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statointervento',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='statointervento',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='statosegnalazione',
            name='created_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statosegnalazione',
            name='descrizione',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='statosegnalazione',
            name='modified_by',
            field=models.CharField(default=None, max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='statosegnalazione',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='statosegnalazione',
            name='note',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
    ]
