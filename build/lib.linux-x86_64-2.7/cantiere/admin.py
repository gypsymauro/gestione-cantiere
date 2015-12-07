from django.contrib import admin

# Register your models here.

from .models import Squadra
from .models import StatoSegnalazione
from .models import Segnalazione
from .models import StatoIntervento
from .models import Intervento
from .models import Risorsa
from .models import InterventoRisorsa
from .models import Costo
from .models import CentroCosto
from .models import Allegato

class InterventoRisorsaInline(admin.TabularInline):
    model = InterventoRisorsa
    exclude = ['created','created_by','modified','modified_by','deleted','note']

    
class RisorsaAdmin(admin.ModelAdmin):
    inlines = (InterventoRisorsaInline,)
    exclude = ['created','created_by','modified','modified_by','deleted']


class InterventoAdmin(admin.ModelAdmin):
    inlines = (InterventoRisorsaInline,)
    list_display = ['oggetto','data_inizio','stato','stampa_intervento']
    list_editable = ['stato']
    ordering = ['created']
    exclude = ['created','created_by','modified','modified_by','deleted']
    list_filter = ('stato','data_inizio','centro_costo','responsabile')
    save_on_top = True
    search_fields = ('oggetto','data_inizio')

admin.site.register(Squadra)
admin.site.register(StatoSegnalazione)
admin.site.register(Segnalazione)
admin.site.register(StatoIntervento)
admin.site.register(Intervento,InterventoAdmin)
admin.site.register(Risorsa,RisorsaAdmin)
admin.site.register(Costo)
admin.site.register(CentroCosto)
admin.site.register(Allegato)
#admin.site.register(InterventoMezzo)
#admin.site.register(InterventoPersona)
