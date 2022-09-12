from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    katalogs = CatalogItem.objects.all()
    konteks = {
        "katalogs" : katalogs,
    }
    return render(request, 'katalog.html', konteks)

