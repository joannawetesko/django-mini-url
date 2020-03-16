from django.urls import path
from miniurl import views

urlpatterns = [
    path('create/<path:link>', views.create_url),
    path('<path:link>', views.redirect_url)
]