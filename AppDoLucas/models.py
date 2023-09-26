from django.db import models

class Idolo(models.Model):
    player = models.CharField(max_length=50)
    titles_won = models.CharField(max_length=70)
    games = models.CharField(max_length=20)
    era = models.CharField(max_length=50)
    position = models.CharField(max_length=20)

class Experiencia(models.Model):
    TYPE_CHAMPIONSHIP = [
        ("M", "Mundial"),
        ("I", "Internacional"),
        ("N", "Nacional"),
    ]
    experiences = models.CharField(max_length=50)
    where = models.CharField(max_length=50)
    with_who = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHAMPIONSHIP)

class Titulo(models.Model):
  campeonato = models.CharField(max_length=50)
  quantidade = models.CharField(max_length=50)


