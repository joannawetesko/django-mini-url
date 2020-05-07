from django.urls import path
from miniurl import views

urlpatterns = [
    path('<path:link>', views.RedirectURLView.as_view(), name='redirect_url'),
    path('', views.MainView.as_view(), name='main')
]