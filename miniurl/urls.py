from django.urls import path
from miniurl import views

urlpatterns = [
    path('<path:link>', views.RedirectURL.as_view(), name='redirect_url'),
    path('', views.Main.as_view(), name='main')
]