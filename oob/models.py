
from django.db import models


class Personne(models.Model):
    nom = models.Charfield(max_lenght=200)