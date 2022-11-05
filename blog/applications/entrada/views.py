#
from django.shortcuts import render

#
from django.views.generic import (
    ListView,
    DetailView
)

# From models
from .models import Category, Entry



class EntryListView(ListView):
    template_name = "entrada/lista.html"
    # definimos una palabra de contexto que se envia al template
    context_object_name = 'entradas'
    paginate_by = 9

    # Enviamos un contexto al template
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        # Recuperamos todas las categorias que tenemos en nuestra base de datos
        context["categorias"] = Category.objects.all()
        return context

    # Cuando se hace un queryset no es necesario especificar un modelo al inicio
    def get_queryset(self):
        # Necesitamos un kword(Palabra clave de busqueda) el cual vamos a recuperar del template
        kword = self.request.GET.get("kword", '')
        # Definimos tambien categoria(Palabra clave de busqueda) para filtrar tambien bajo ese parametro template
        categoria = self.request.GET.get("categoria", '')
        # Hacemos la busqueda en nuestra base de datos
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado


# Vista para ver el detalle de las entradas
class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
