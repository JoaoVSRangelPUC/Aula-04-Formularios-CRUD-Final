from django.db import models

class Mapas(models.Model):
  name = models.CharField(max_length=50)
  local = models.CharField(max_length=50)
  modos = models.CharField(max_length=50)

class Armas(models.Model):
  nome = models.CharField(max_length=50)
  origem = models.CharField(max_length=3)
  calibre = models.CharField(max_length=50)

class TabelaMapas(models.Model):
  nome = models.CharField(max_length=100)
  local = models.CharField(max_length=100)
