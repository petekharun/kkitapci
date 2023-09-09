from django.core.exceptions import BadRequest

from kitap.models import Kitap


def kitapci_queryset_filter(request):
    queryset = Kitap.objects.all()
    stok = request.query_params.get('stok')
    if stok is not None:
        try:
            queryset = queryset.filter(stok=stok)
        except:
            raise BadRequest("Invalid stok value")
    dil = request.query_params.get('dil')
    if dil is not None:
        try:
            queryset = queryset.filter(dil__icontains=dil)
        except:
            raise BadRequest("Invalid dil value")
    yazar = request.query_params.get("yazar")
    if yazar is not None:
        try:
            queryset = queryset.filter(yazar__contains=yazar)
        except:
            raise BadRequest("Invalid yazar value")
    tur = request.query_params.get("tur")
    if tur is not None:
        try:
            queryset = queryset.filter(tur__contains=tur)
        except:
            raise BadRequest("Invalid tur value")
    keyword = request.query_params.get("keyword")
    if keyword is not None:
        queryset = queryset.filter(aciklama__icontains=keyword)
    queryset = queryset.order_by("-id")
    return queryset