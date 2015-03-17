from django.contrib import admin

from polls.models import Ticket, Personne

class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 10


class PersonneInline(admin.TabularInline):
    model = Personne
    extra = 5