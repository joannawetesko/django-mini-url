from django.apps import AppConfig
from .miniurl import URLEncoder

class MiniurlConfig(AppConfig):
    name = 'miniurl'
    encoder = URLEncoder()
