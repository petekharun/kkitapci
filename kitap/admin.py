from django.contrib import admin

from .models import Kitap, Yazar


# Register your models here.

class KitapAdmin(admin.ModelAdmin):
    list_display = ('isim', 'yazar', 'sayfa_sayisi', 'yayin_tarihi', 'tur', 'fiyat', 'stok', 'dil')


admin.site.register(Kitap, KitapAdmin)


admin.site.register(Yazar)
