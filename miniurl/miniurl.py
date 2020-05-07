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

    @staticmethod
    def get_url_object(pk):
        url_object = get_object_or_404(URL, pk=pk)
        return url_object

    def encode_url(self, url):
        url_pk = self.create_url_object(url)
        shortened_url = self.HASHIDS.encode(url_pk)
        return shortened_url

    def decode_url(self, shortened_url):
        try:
            url_pk = self.HASHIDS.decode(shortened_url)[self.URL_INDEX]
            return self.get_url_object(url_pk)
        except IndexError:
            raise Http404("This link does not exist.")