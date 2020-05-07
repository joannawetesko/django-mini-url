from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import RedirectView, CreateView

from .apps import MiniurlConfig
from .models import URL


class MainView(CreateView):
    template_name = 'main.html'
    model = URL
    fields = ['url']

    def form_valid(self, form):
        shortened_link = self.generate_short_link(form.cleaned_data.get('url'))
        return render(self.request, 'success.html', {'shortened_link': shortened_link})

    def generate_short_link(self, url):
        shortened_link = MiniurlConfig.encoder.encode_url(url)
        return f"{self.request.scheme}://{self.request.get_host()}{self.request.path}{shortened_link}"


class RedirectURLView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        try:
            decoded_url = MiniurlConfig.encoder.decode_url(self.kwargs.get('link'))
            if decoded_url.is_valid():
                self.url = decoded_url.url
            else:
                return HttpResponseForbidden("This link has expired. Please generate a new link.")
        except IndexError:
            raise Http404("This link does not exist.")

        return super().get_redirect_url(*args, **kwargs)
