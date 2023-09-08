from django.db import models


# Create your models here.

class Kitap(models.Model):
    isim = models.CharField(max_length=50, blank=True, null=True)
    yazar = models.CharField(max_length=40, blank=True, null=True)
    sayfa_sayisi = models.IntegerField(blank=True, null=True)
    yayin_tarihi = models.DateTimeField(blank=True, null=True)
    tur = models.CharField(max_length=15, blank=True, null=True)
    fiyat = models.IntegerField(blank=True, null=True)
    stok = models.BooleanField(blank=True, null=True)
    aciklama = models.TextField()
    dil = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.isim + self.yazar


class Yazar(models.Model):
    adi_soyadi = models.CharField(max_length=50, blank=True, null=True)
    aciklama = models.TextField()

    def __str__(self):
        return self.adi_soyadi

