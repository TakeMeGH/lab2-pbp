from django.test import TestCase, Client
from django.urls import reverse
from katalog.models import CatalogItem
from katalog.views import show_katalog

class TestModels(TestCase):
    
    def test_katalog_GET(self):
        client = Client()
        response = client.get(reverse("katalog:show_katalog_urls"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'katalog.html')
        self.assertTemplateUsed(response, 'base.html')
