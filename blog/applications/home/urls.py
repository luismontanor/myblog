#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'register-suscription',
        views.SuscriberCreateView.as_view(),
        name='add_suscription',
    ),
    path(
        'contact',
        views.ContactCreateView.as_view(),
        name='contact',
    ),
]