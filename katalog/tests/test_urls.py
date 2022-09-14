from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestUrls(SimpleTestCase):

    def test_show_katalog_is_resolved(self):
        url = reverse('katalog:show_katalog_urls')
        self.assertEqual(resolve(url).func, show_katalog)
