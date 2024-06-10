from django.db import models

# Create your models here.
class Nauczyciel(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=100, null=False)
    pesel = models.CharField(max_length=11, null=False)

class Uczen(models.Model):
    ...

class Ocena(models.Model):
    ...

class Klasa(models.Model):
    ...

class Przedmiot(models.Model):
    ...
