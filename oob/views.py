from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from oob.models import Ticket



def index(request):
    message = "Coucou"
    return render(request, 'oob/index.html', {'bob': message})

def demande(request):

    return render(request, 'oob/demande.html',)

def resultat(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    return render(request, 'oob/resultat.html', {'ticket': ticket})

def traitement_de_demande(request):
    nom = request.POST['nom']
    courriel = request.POST['courriel']
    message = request.POST['message']
    ticket = Ticket()
    ticket.demandes = message
    ticket.courriel = courriel
    ticket.demandeur = nom
    ticket.date_de_soumission = timezone.now()
    ticket.save()

    return HttpResponseRedirect(reverse('resultat', args=(ticket.id,)))