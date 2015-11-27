from django.shortcuts import render
from .models import *
# Create your views here.
# per la generazione delle schede

# pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle


from django.http import HttpResponse
from io import BytesIO

PDF_MARGIN=2*cm
def home(request):
    return render(request, 'home.html', {})

def interventi(request):
    interventi = Intervento.objects.all
    return render(request, 'interventi.html', {'interventi':interventi})


def crea_pagina(doc,intervento):
    parts = []

    data = [[ 'SCHEDA LAVORO N.: ____', 'DEL: __________']]
    t = Table(data,colWidths=doc.width/2)
    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))

    parts.append(t)
    parts.append(Spacer(1, 0.5 * cm))

    persone = ''
    mezzi = ''
    persone_ore = ''
    mezzi_ore = ''
    for risorsa in intervento.risorse.all():
        if risorsa.tipo == 'persona':
            persone += risorsa.nome + '\n'
            persone_ore += 'dalle:[_____] alle:[_____]\n'
        if risorsa.tipo == 'mezzo':
            mezzi += risorsa.nome + '\n'
            mezzi_ore += '[_______]\n'
    data = [
        ['PERSONE', 'ORARIO DI LAVORO', 'MEZZI', 'ORE'],
        [persone, persone_ore,mezzi,mezzi_ore],
        ]


#    table = Table(data, [3 * cm, 1.5 * cm, cm])
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('ALIGN', (0,0), (-1,-1),'CENTER'),
        ]))
    parts.append(t)

    data = [['DESCRIZIONE DEL LAVORO'],[intervento.descrizione + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n']]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('ALIGN', (0,0), (-1,-1),'CENTER'),
        ]))
    parts.append(t)


    data = [
        ['SOSPESO IL\n\n\n','RIPRESO IL\n\n\n','CONCLUSO IL\n\n\n'],
#        ['','',''],
        ]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('ALIGN', (0,0), (-1,-1),'CENTER'),
        ]))
    parts.append(t)


    data = [
        ['MOTIVO DELLA SOSPENSIONE'],
        ['\n\n\n\n\n\n\n'],
        ]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('ALIGN', (0,0), (-1,-1),'CENTER'),
        ]))
    parts.append(t)

    data = [
        ['NOTE:', ' ATTREZZI PARTICOLARI:'],
        ['\n\n\n\n\n\n', '\n\n\n\n\n\n'],
        ]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))
    parts.append(t)


    data = [
        ['COSTO MATERIALI IMPIEGATI (n fatt.):', ''],
        ['VARIE:\n', '\n'],
        ]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))
    parts.append(t)


    campofirma ='FIRMA DEL CAPO SQUADRA:\n[%s]' % intervento.responsabile 
    data = [
        [campofirma, '\n'],
        ]
    t = Table(data,colWidths=doc.width/len(data[0]))

    t.setStyle(TableStyle([
        ('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))
    parts.append(t)
        
                
    doc.build(parts)    

def stampa_scheda(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    interventi = Intervento.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="stampascheda.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                        rightMargin=PDF_MARGIN, leftMargin=PDF_MARGIN,
                        topMargin=PDF_MARGIN, bottomMargin=PDF_MARGIN,)


    crea_pagina(doc, interventi[0])
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
