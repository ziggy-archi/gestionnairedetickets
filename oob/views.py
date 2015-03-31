from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from oob.models import Ticket


class MessageErreur(object):
    def __init__(self):
        self.nom = "Veuillez renseigner le nom"
        self.courriel = "Veuillez renseigner le courriel"
        self.message = "Veuillez decrire le problème"
        self.affiche_nom = False
        self.affiche_courriel = False
        self.affiche_message = False


class TempTicket(object):
     def __init__(self):
        self.nom = ""
        self.courriel = ""
        self.message = ""


def index(request):
    message = "Coucou"
    return render(request, 'oob/index.html', {'bob': message})

def demande(request,):

    return render(request, 'oob/demande.html',)

def resultat(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    return render(request, 'oob/resultat.html', {'ticket': ticket})

def traitement_de_demande(request):
    temp_ticket = TempTicket()
    temp_ticket.nom = request.POST['nom']
    temp_ticket.courriel = request.POST['courriel']
    temp_ticket.message = request.POST['message']

    erreur = False
    message_erreur = MessageErreur()

    if str.strip(temp_ticket.nom) == "":
        message_erreur.affiche_nom = True
        erreur = True

    if str.strip(temp_ticket.courriel) == "":
        message_erreur.affiche_courriel = True
        erreur = True

    if str.strip(temp_ticket.message) == "":
        message_erreur.affiche_message = True
        erreur = True

    if erreur:
        return render(request, 'oob/demande.html', {'message_erreur': message_erreur, 'temp_ticket': temp_ticket})

    ticket = Ticket()
    ticket.demandes = temp_ticket.message
    ticket.courriel = temp_ticket.courriel
    ticket.demandeur = temp_ticket.nom
    ticket.date_de_soumission = timezone.now()
    ticket.save()
    return HttpResponseRedirect(reverse('resultat', args=(ticket.id,)))