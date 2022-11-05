#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/',
        views.EntryListView.as_view(),
        name='entry_lista',
    ),
    path(
        'entrada-detalle/<slug>',
        views.EntryDetailView.as_view(),
        name='entry_detail',
    ),
]