from django.db import models


class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Marka(models.Model):
    def __str__(self):
        return str(self.nazwa)

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Marki"


class Model(models.Model):
    def __str__(self):
        return str(self.nazwa)

    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Modele"


class Samochody(models.Model):
    def __str__(self):
        return str(self.nazwa)

    kategoria = models.ForeignKey(Kategoria, blank=True, on_delete=models.CASCADE, null=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=50)
    rok = models.DecimalField(max_digits=4, decimal_places=0)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"
