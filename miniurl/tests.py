from django.test import TestCase, RequestFactory
from django.utils import timezone

from model_mommy import mommy
from hashids import Hashids

from .models import URL
from .miniurl import URLEncoder
from .views import MainView


class URLTestCase(TestCase):

    def setUp(self):
        self.url = mommy.make(URL, url="http://www.google.com")
        self.expired_url = mommy.make(
            URL,
            url="http://www.google.com",
            date_created=timezone.now() - timezone.timedelta(days=11),
            url_expires=timezone.now() - timezone.timedelta(days=10)
        )

    def test_url_is_valid(self):
        self.assertTrue(self.url.is_valid())
        self.assertFalse(self.expired_url.is_valid())

class MiniURLTestCase(TestCase):

    def setUp(self):
        self.url = "http://www.google.com"
        self.encoder = URLEncoder()

    def test_encode_url(self):
        shortened_url = self.encoder.encode_url(self.url)
        url_object = URL.objects.get(url=self.url)

        self.assertIsNotNone(url_object)
        self.assertEquals(shortened_url, Hashids(min_length=16).encode(url_object.pk))

    def test_decode_url(self):
        url_object = mommy.make(URL, url="http://www.google.com")
        shortened_url = Hashids(min_length=16).encode(url_object.pk)

        self.assertEquals(self.encoder.decode_url(shortened_url), url_object)


class ViewsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.encoder = URLEncoder()

        self.url_object = mommy.make(URL, url="http://www.google.com")
        self.encoded_url = Hashids(min_length=16).encode(self.url_object.pk)

    def test_link_generation(self):
        main = MainView()
        main.request = self.factory.get("")
        self.assertEquals(
            main.generate_short_link(self.url_object.url),
            "http://testserver/O3GWpmbk5ezJn4KR"
        )
