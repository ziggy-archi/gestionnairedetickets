from django.contrib import admin

from oob.models import Ticket, Personne

class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_filter = ['date_de_soumission']
    list_display = ('personne', 'date_de_soumission', 'cloture_du_ticket')



class PersonneInline(admin.TabularInline):
    model = Personne
    extra = 5


class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Personne, PersonneAdmin)