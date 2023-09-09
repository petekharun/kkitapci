import datetime

import xlwt
from django.contrib import admin
from django.http import HttpResponse

from .models import Kitap, Yazar


# Register your models here.

class KitapAdmin(admin.ModelAdmin):
    list_display = ('isim', 'yazar', 'sayfa_sayisi', 'yayin_tarihi_display', 'tur', 'fiyat_display', 'stok', 'dil')
    list_filter = ("yayin_tarihi", "tur", "stok", "dil")

    def fiyat_display(self, obj):
        return f'{obj.fiyat} ₺'

    fiyat_display.short_description = "Fiyat"

    def yayin_tarihi_display(self, obj):
        return f'{obj.yayin_tarihi.strftime("%d/%m/%y")}'

    yayin_tarihi_display.short_description = "Yayin Tarihi"

    actions = ['export_selected_to_xls']

    def export_selected_to_xls(self, request, queryset):
        current_tine = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="kitaplar_{}.xls"'.format(current_tine)

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Kitaplar")

        row_num = 0

        columns_name = ['ID', 'İsim', 'Yazar', 'Sayfa Sayısı', 'Yayın Tarihi', 'Tür', 'Fiyat', 'Stok', 'Dil']

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num, column_name in enumerate(columns_name):
            ws.write(row_num, col_num, column_name, font_style)

        font_style = xlwt.XFStyle()

        for row in queryset.values_list('id', 'isim', 'yazar', 'sayfa_sayisi', 'yayin_tarihi', 'tur', 'fiyat', 'stok',
                                        'dil'):
            row_num += 1
            for col_num, value in enumerate(row):
                ws.write(row_num, col_num, str(value), font_style)

        wb.save(response)
        return response

    export_selected_to_xls.short_description = "Seçilenleri Excel'e Aktar"


admin.site.register(Kitap, KitapAdmin)

admin.site.register(Yazar)
