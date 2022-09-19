from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers


def show_mywatchlist(request):
    watchlistItem = MywatchlistItem.objects.all()
    banyak_ditonton = 0
    for obj in watchlistItem:
        banyak_ditonton += obj.watched == True
    is_banyak_tonton = (banyak_ditonton * 2 >= len(watchlistItem))
    konteks = {
        "watchlistItem" : watchlistItem,
        "is_banyak_tonton" : is_banyak_tonton,
    }
    return render(request, 'mywatchlist.html', konteks)
 

def show_xml(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

