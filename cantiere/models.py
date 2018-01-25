from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from datetime import datetime
from crum import get_current_user, get_current_request
from django.db.models import Q

TEXTFIELD_MAXLENGHT=512
CHARFIELD_MAXLENGHT=300

class Base(models.Model):
    note = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True)    
    deleted = models.BooleanField(default = False)
    created = models.DateTimeField(null=True, blank = True)
    created_by = models.CharField(max_length=CHARFIELD_MAXLENGHT, blank=True, null=True,default=None)
    modified = models.DateTimeField(null=True, blank = True)
    modified_by = models.CharField(max_length=CHARFIELD_MAXLENGHT, blank=True, null=True,default=None)

    def save(self, *args, **kwargs):
        ### vengono aggiunti l'ip l'utente e la data di modifica/creazione in automatico
        request = get_current_request()
        if request:
            remote_addr = request.META['REMOTE_ADDR']
        
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user.get_username() + '[' + remote_addr + ']'
            self.created = datetime.now()
        self.modified_by = user.get_username() + '[' + remote_addr + ']'
        self.modified = datetime.now()        
        super(Base, self).save(*args, **kwargs)        

    # non funziona da admin perche viene usato un "bulk"
    def delete(self, *args, **kwargs):
        self.deleted = True
        #if not self.related_query.all():
        #    super(Base, self).delete(*args, **kwargs)
        
    class Meta:
        abstract = True    
        
class Costo(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    valore = models.IntegerField(default=0)
    dal = models.DateTimeField('Valido dal',blank=True)
    al = models.DateTimeField('Valido al', blank=True,null=True)
    SCELTA_TIPO=(
        ('ORA','ORARIO'),
        ('KM','AL KM'),
        )
    tipo = models.CharField(max_length=3,choices=SCELTA_TIPO, default='ORARIO')
    def __str__(self):
        return self.nome + '[ ' + str(self.valore) + '/' + self.tipo + ' ]'

    class Meta(object):
        verbose_name = 'Tipo di costo'
        verbose_name_plural = 'Tipo di costo'



class Allegato(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    documento = models.FileField()
    descrizione = models.TextField(max_length=TEXTFIELD_MAXLENGHT)
    def __str__(self):
        return self.nome + ' ' + self.descrizione

    class Meta(object):
        verbose_name = 'Allegato'
        verbose_name_plural = 'File Allegati'

    
class Risorsa(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    costo = models.ForeignKey(Costo, blank=True,on_delete=models.CASCADE)
    targa = models.CharField(max_length=CHARFIELD_MAXLENGHT, blank=True)
    codice_protocollo = models.CharField(max_length=CHARFIELD_MAXLENGHT, blank=True)
    TIPO_RISORSA=(
        ('persona','Persona'),
        ('mezzo','Mezzo'),
        ('attrezzatura','Attrezzatura'),
        ('ditta','Ditta'),
        ('altro','Altro'),        
    )
    tipo = models.CharField(max_length=CHARFIELD_MAXLENGHT,choices=TIPO_RISORSA, default='persona')

    def __str__(self):
        return self.nome 

    def save(self, *args, **kwargs):
        self.nome = self.nome and self.nome.upper()        
        super(Risorsa, self).save(*args, **kwargs)


    @property
    def get_costo(self,date = datetime.now()):
        ret = self.costo
        return ret.valore
    
         
    class Meta(object):
        verbose_name = 'Risorsa'
        verbose_name_plural = 'Risorse'


        
        
class Squadra(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    risorse = models.ManyToManyField(Risorsa)
    def __str__(self):
        return self.nome
    class Meta(object):
        verbose_name = 'Squadra'
        verbose_name_plural = 'Squadre'


class StatoSegnalazione(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    descrizione = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True)    
    def __str__(self):
        return self.nome
    class Meta(object):
        verbose_name = 'Stato della segnalazione'
        verbose_name_plural = 'Stati della segnalazione'
    
        
class Segnalazione(Base):
    oggetto = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    segnalatore = models.CharField(max_length=CHARFIELD_MAXLENGHT,blank = True)        
    descrizione = models.CharField(max_length=CHARFIELD_MAXLENGHT,blank = True)
    descrizione_interna = models.TextField(max_length=TEXTFIELD_MAXLENGHT,blank = True)
    data_inserimento = models.DateTimeField('Data di inserimento',blank = True, null = True)
    data_chiusura = models.DateTimeField('Data di chiusura',blank = True, null = True)    
    stato = models.ForeignKey(StatoSegnalazione, default=1,blank = True,on_delete=models.CASCADE)        
    allegati = models.ManyToManyField(Allegato, blank = True)
    def __str__(self):
        return self.oggetto + '[' + str(self.stato) + ']'

    class Meta(object):
        verbose_name = 'Segnalazione'
        verbose_name_plural = 'Segnalazioni'
    
    
class StatoIntervento(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT)
    descrizione = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True)        
    def __str__(self):
        return self.nome
    class Meta(object):
        verbose_name = 'Stato intervento'
        verbose_name_plural = 'Stati degli interventi'

class CentroCosto(Base):
    nome = models.CharField(max_length=CHARFIELD_MAXLENGHT,default='', blank = True)
    descrizione = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True)  
    def __str__(self):
        return self.nome

    class Meta(object):
        verbose_name = 'Centro di costo'
        verbose_name_plural = 'Centri di costo'

class Intervento(Base):
    oggetto = models.CharField(max_length=CHARFIELD_MAXLENGHT,default='', blank = True)
    descrizione = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True)
    descrizione_interna = models.TextField(max_length=TEXTFIELD_MAXLENGHT,default='', blank = True, null = True)        
    segnalazione = models.ForeignKey(Segnalazione,on_delete=models.CASCADE)
    risorse = models.ManyToManyField(Risorsa, through='InterventoRisorsa', blank = True)
    stato = models.ForeignKey(StatoIntervento,default=1,blank = True, null = True,on_delete=models.CASCADE)
    data_inizio = models.DateTimeField('Data di inizio',blank = True, null = True)
    data_sospensione = models.DateTimeField('Data di sospensione',blank = True, null = True)
    data_riapertura = models.DateTimeField('Data di riapertura',blank = True, null = True)
    data_chiusura = models.DateTimeField('Data di chiusura',blank = True, null = True)
    centro_costo = models.ForeignKey(CentroCosto, blank = True, null = True,on_delete=models.CASCADE)
    allegati = models.ManyToManyField(Allegato, blank = True)
    responsabile = models.ForeignKey(Risorsa, related_name='intervento_responsabile', blank = True, null = True, limit_choices_to = {'tipo':'persona'},on_delete=models.CASCADE)
    buoni = models.CharField(max_length=CHARFIELD_MAXLENGHT,blank = True)
    spese = models.CharField(max_length=CHARFIELD_MAXLENGHT,blank = True)
    beneficiario = models.CharField(max_length=CHARFIELD_MAXLENGHT,default='', blank = True)
    def __str__(self):
        return str(self.oggetto) + '(' + str(self.segnalazione) + ') [' + str(self.stato) +']'

    def stampa_intervento(self):
        return '<a href="/stampa_scheda?id=%s">Stampa</a>' % self.id
    stampa_intervento.allow_tags = True #this is to allow HTML tags.
    stampa_intervento.short_description = 'Stampa'    

    class Meta(object):
        verbose_name = 'Intervento'
        verbose_name_plural = 'Interventi'

    @property
    def costo(self):
        "Ritorna il costo totale"
        risorse = self.risorse.all()
        costo_tot = 0
        for risorsa in risorse:
            relazioni = InterventoRisorsa.objects.filter(intervento=self, risorsa=risorsa)

            for relazione in relazioni.all():
                costo_tot += risorsa.get_costo * relazione.impiego



        return costo_tot
       


        
        


class InterventoRisorsa(Base):
    risorsa = models.ForeignKey(Risorsa,on_delete=models.CASCADE)
    intervento = models.ForeignKey(Intervento,on_delete=models.CASCADE)    
    impiego = models.IntegerField('# ore o km',default=0)

    class Meta(object):
        verbose_name = 'Risorsa x intervento'
        verbose_name_plural = 'Risorse usate'

