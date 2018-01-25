# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allegato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('documento', models.FileField(upload_to=b'')),
                ('descrizione', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name': 'Allegato',
                'verbose_name_plural': 'Allegati',
            },
        ),
        migrations.CreateModel(
            name='CentroCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(default=b'', max_length=300, blank=True)),
                ('descrizione', models.TextField(default=b'', max_length=512, blank=True)),
            ],
            options={
                'verbose_name': 'Centro di costo',
                'verbose_name_plural': 'Centri di costo',
            },
        ),
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('valore', models.IntegerField(default=0)),
                ('dal', models.DateTimeField(verbose_name=b'Valido dal', blank=True)),
                ('al', models.DateTimeField(null=True, verbose_name=b'Valido al', blank=True)),
                ('tipo', models.CharField(default=b'ORARIO', max_length=3, choices=[(b'ORA', b'ORARIO'), (b'KM', b'AL KM')])),
            ],
            options={
                'verbose_name': 'Tipo di costo',
                'verbose_name_plural': 'Tipo di costo',
            },
        ),
        migrations.CreateModel(
            name='Intervento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('oggetto', models.CharField(default=b'', max_length=300, blank=True)),
                ('descrizione', models.TextField(default=b'', max_length=512, blank=True)),
                ('descrizione_interna', models.TextField(default=b'', max_length=512, null=True, blank=True)),
                ('data_inizio', models.DateTimeField(null=True, verbose_name=b'Data di inizio', blank=True)),
                ('data_sospensione', models.DateTimeField(null=True, verbose_name=b'Data di sospensione', blank=True)),
                ('data_riapertura', models.DateTimeField(null=True, verbose_name=b'Data di riapertura', blank=True)),
                ('data_chiusura', models.DateTimeField(null=True, verbose_name=b'Data di chiusura', blank=True)),
                ('buoni', models.CharField(max_length=300, blank=True)),
                ('spese', models.CharField(max_length=300, blank=True)),
                ('beneficiario', models.CharField(default=b'', max_length=300, blank=True)),
                ('allegati', models.ManyToManyField(to='cantiere.Allegato', blank=True)),
                ('centro_costo', models.ForeignKey(blank=True, to='cantiere.CentroCosto', null=True,on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Intervento',
                'verbose_name_plural': 'Interventi',
            },
        ),
        migrations.CreateModel(
            name='InterventoRisorsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('ore', models.IntegerField(default=0)),
                ('minuti', models.IntegerField(default=0)),
                ('intervento', models.ForeignKey(to='cantiere.Intervento',on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Risorsa x intervento',
                'verbose_name_plural': 'Risorse usate',
            },
        ),
        migrations.CreateModel(
            name='Risorsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('targa', models.CharField(max_length=300, blank=True)),
                ('codice_protocollo', models.CharField(max_length=300, blank=True)),
                ('tipo', models.CharField(default=b'persona', max_length=300, choices=[(b'persona', b'Persona'), (b'mezzo', b'Mezzo'), (b'attrezzatura', b'Attrezzatura'), (b'ditta', b'Ditta'), (b'altro', b'Altro')])),
                ('costo', models.ForeignKey(to='cantiere.Costo', blank=True,on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Risorsa',
                'verbose_name_plural': 'Risorse',
            },
        ),
        migrations.CreateModel(
            name='Segnalazione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('oggetto', models.CharField(max_length=300)),
                ('segnalatore', models.CharField(max_length=300, blank=True)),
                ('descrizione', models.CharField(max_length=300, blank=True)),
                ('descrizione_interna', models.TextField(max_length=512, blank=True)),
                ('data_inserimento', models.DateTimeField(null=True, verbose_name=b'Data di inserimento', blank=True)),
                ('data_chiusura', models.DateTimeField(null=True, verbose_name=b'Data di chiusura', blank=True)),
                ('allegati', models.ManyToManyField(to='cantiere.Allegato', blank=True)),
            ],
            options={
                'verbose_name': 'Segnalazione',
                'verbose_name_plural': 'Segnalazioni',
            },
        ),
        migrations.CreateModel(
            name='Squadra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('risorse', models.ManyToManyField(to='cantiere.Risorsa')),
            ],
            options={
                'verbose_name': 'Squadra',
                'verbose_name_plural': 'Squadre',
            },
        ),
        migrations.CreateModel(
            name='StatoIntervento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('descrizione', models.TextField(default=b'', max_length=512, blank=True)),
            ],
            options={
                'verbose_name': 'Stato intervento',
                'verbose_name_plural': 'Stati degli interventi',
            },
        ),
        migrations.CreateModel(
            name='StatoSegnalazione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', max_length=512, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
                ('modified_by', models.CharField(default=None, max_length=300, null=True, blank=True)),
                ('nome', models.CharField(max_length=300)),
                ('descrizione', models.TextField(default=b'', max_length=512, blank=True)),
            ],
            options={
                'verbose_name': 'Stato della segnalazione',
                'verbose_name_plural': 'Stati della segnalazione',
            },
        ),
        migrations.AddField(
            model_name='segnalazione',
            name='stato',
            field=models.ForeignKey(default=1, blank=True, to='cantiere.StatoSegnalazione',on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='interventorisorsa',
            name='risorsa',
            field=models.ForeignKey(to='cantiere.Risorsa',on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='intervento',
            name='responsabile',
            field=models.ForeignKey(related_name='intervento_responsabile', blank=True, to='cantiere.Risorsa', null=True,on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='intervento',
            name='risorse',
            field=models.ManyToManyField(to='cantiere.Risorsa', through='cantiere.InterventoRisorsa', blank=True),
        ),
        migrations.AddField(
            model_name='intervento',
            name='segnalazione',
            field=models.ForeignKey(to='cantiere.Segnalazione',on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='intervento',
            name='stato',
            field=models.ForeignKey(default=1, blank=True, to='cantiere.StatoIntervento', null=True,on_delete=models.CASCADE),
        ),
    ]
