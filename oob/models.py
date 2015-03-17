
from django.db import models


class Personne(models.Model):
    nom = models.CharField(max_length=200)

class Ticket(models.Model):
    demandes = models.CharField(max_length=200)
    cloture_du_ticket = models.CharField(max_length=20)
    date_de_soumission = models.DateTimeField()
    personne = models.ForeignKey(Personne)
