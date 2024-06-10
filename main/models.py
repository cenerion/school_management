from django.db import models


GENDER_CHOICES = {
        'M': 'Male',
        'F': 'Female',
}


class Nauczyciel(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=100, null=False)
    data_ur = models.DateField()
    plec = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Klasa(models.Model):
    profil = models.CharField(max_length=50, null=False)
    wychowawca = models.ForeignKey(Nauczyciel, on_delete=models.PROTECT)
    symbol = models.CharField(max_length=5, null=False)


class Uczen(models.Model):
    imie = models.CharField(max_length=50, null=False)
    nazwisko = models.CharField(max_length=100, null=False)
    data_ur = models.DateField()
    plec = models.CharField(max_length=1, choices=GENDER_CHOICES)
    klasa = models.ForeignKey(Klasa, on_delete=models.PROTECT, null=True, blank=True)
    adres_zam = models.CharField(max_length=255)

    def get_fields():
        return [field.name for field in Uczen._meta.fields]


class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=50, null=False)


class Ocena(models.Model):
    uczen = models.ForeignKey(Uczen, on_delete=models.PROTECT)
    nauczyciel = models.ForeignKey(Nauczyciel, on_delete=models.PROTECT)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.PROTECT)
    wartosc = models.FloatField()
    nazwa = models.CharField(max_length=50, null=False)
    data_wyst = models.DateField(max_length=255)