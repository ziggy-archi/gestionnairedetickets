from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404



def index(request):
    message = "Un message"
    return render(request, 'oob/index.html', {'message': message})

def demande(request):

    return render(request, 'oob/demande.html',)

def resultat(request):

    return render(request, 'oob/resultat.html',)

def traitement_de_demande(request):
    nom = request.POST['nom']
    return render(request, 'oob/traitement_de_demande.html',)