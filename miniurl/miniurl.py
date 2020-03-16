from hashids import Hashids
from .models import URL


hashids = Hashids(min_length=16)


def encode_url(url, user):
    url_object = URL(
        url=url,
        user=user
    )
    url_object.save()
    shortened_url = hashids.encode(url_object.pk)
    return shortened_url


def decode_url(shortened_url):
    pk = hashids.decode(shortened_url)[0]
    url_object = URL.objects.get(pk=pk)
    return url_object.url
