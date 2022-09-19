from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.models import MywatchlistItem
from mywatchlist.views import show_mywatchlist

class TestModels(TestCase):
    
    def test_mywatchlist_GET(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mywatchlist.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_mywatchlist_json(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_mywatchlist_xml(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)
