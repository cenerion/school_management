from django.db import models


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Nauczyciel(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=100, null=False)
    data_ur = models.DateField()
    plec = models.Choices(GENDER_CHOICES)


class Klasa(models.Model):
    profil = models.CharField(max_length=50, null=False)
    wychowawca = models.ForeignKey(Nauczyciel, on_delete=models.SET_NULL)
    symbol = models.CharField(max_length=5, null=False)


class Uczen(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=100, null=False)
    data_ur = models.DateField()
    plec = models.Choices(GENDER_CHOICES)
    klasa_F = models.ForeignKey(Klasa, on_delete=models.SET_NULL)
    adres_zam = models.CharField()


class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=50, null=False)


class Ocena(models.Model):
    uczen = models.ForeignKey(Uczen)
    nauczyciel = models.ForeignKey(Nauczyciel)
    przedmiot = models.ForeignKey(Przedmiot)
    wartosc = models.FloatField()
    nazwa = models.CharField(max_length=50, null=False)
    data_wyst = models.DateField()