
from django.db import models


class Personne(models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Ticket(models.Model):
    demandes = models.TextField(max_length=200)
    cloture_du_ticket = models.BooleanField(default=False)
    date_de_soumission = models.DateTimeField()
    personne = models.ForeignKey(Personne)


