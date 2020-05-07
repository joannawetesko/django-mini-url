from django.http import Http404
from django.shortcuts import get_object_or_404
from hashids import Hashids

from .models import URL

class URLEncoder:

    def __init__(self):
        self.HASHIDS = Hashids(min_length=16)
        self.URL_INDEX = 0

    @staticmethod
    def create_url_object(url):
        url_object = URL(url=url)
        url_object.save()
        return url_object.pk

    def encode_url(self, url):
        url_pk = self.create_url_object(url)
        shortened_url = self.HASHIDS.encode(url_pk)
        return shortened_url

    def decode_url(self, shortened_url):
        url_pk = self.HASHIDS.decode(shortened_url)[self.URL_INDEX]
        return get_object_or_404(URL, pk=url_pk)