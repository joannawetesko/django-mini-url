from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView

from .apps import MiniurlConfig
from .models import URL


class Main(CreateView):
    template_name = 'main.html'
    model = URL
    fields = ['url']

    def form_valid(self, form):
        shortened_link = self.generate_short_link(form.cleaned_data.get('url'))
        return render_to_response('success.html', {'shortened_link': shortened_link})

    def generate_short_link(self, url):
        shortened_link = MiniurlConfig.encoder.encode_url(url)
        return f"{self.request.scheme}://{self.request.get_host()}{self.request.path}{shortened_link}"


class RedirectURL(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        try:
            self.url = MiniurlConfig.encoder.decode_url(self.kwargs.get('link'))
        except IndexError:
            raise Http404("This link does not exist.")
        return super().get_redirect_url(*args, **kwargs)
