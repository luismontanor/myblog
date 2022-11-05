import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

# Apps entrada
from applications.entrada.models import Entry
# Apps Home
from applications.home.models import Home
# From forms
from .forms import SuscriberForm, ContactForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        # Podemos enviar cualquier cosa como contexto(listas, formularios, objetos, diccionarioss)
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        context["home"] = Home.objects.latest('-created')
        # Contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # Contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # Contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # Enviamos formulario de suscripción
        context["form"] = SuscriberForm

        return context


# Vista para el formulario modal de Suscribirme
class SuscriberCreateView(CreateView):
    form_class = SuscriberForm
    success_url = '.'


# Degfinicion la vista para el footer -> Formulario de contacto
class ContactCreateView(CreateView):
    # Importamos nuestro ContactForm
    form_class = ContactForm
    success_url = '.'