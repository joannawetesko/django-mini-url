from django.http import HttpResponse
from django.shortcuts import redirect
from .miniurl import encode_url, decode_url


def create_url(request, link):
    if request.user.is_authenticated:
        shortened_link = encode_url(link, request.user)
        print(shortened_link)
        return HttpResponse(shortened_link)
    else:
        return HttpResponse('unauthorized')


def redirect_url(link):
    try:
        real_link = decode_url(link)
        # TODO: check all the permissions
        return redirect(real_link)
    except Exception as e:
        return HttpResponse(e.args)