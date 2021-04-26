from django.forms import TextInput, Textarea
from django.contrib import admin
from .models import *

class pax_tickets_inline(admin.StackedInline):
    model = ticket_pax
    extra = 1
    max_num = 9

@admin.register(tickets_list)
class list_view(admin.ModelAdmin):
    list_display = [
        'date',
        'cia',
        'agencia',
        'localizador',
        'nome_pax',
        'total',
    ]
    fields = [
        ('localizador', 'agencia', 'fornecedor', 'conta_vinculada'), #mesma linha
        ('milhar', 'taxas', 'cartao', 'adicional'),
        ('anexo'),
        ('obs'),
    ]
    inlines = [pax_tickets_inline]
    list_filter = ('date', 'agencia', 'conta_vinculada',)
    list_per_page = 20
    date_hierarchy = 'date'
    search_fields = ('localizador',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'7'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':40})},
    }


admin.site.register(company)
admin.site.register(distribute)
admin.site.register(ticket_account)
admin.site.register(miles_currency)
admin.site.register(card_used)