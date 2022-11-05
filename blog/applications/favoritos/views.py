from django.shortcuts import render
from django.http import HttpResponseRedirect
#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
#
from django.views.generic import (
    View,
    ListView,
)

# From models
from .models import Favorites


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    # Siempre que utilicemos LoginRequiredMixin hay que especificar un login_url
    login_url = reverse_lazy('users_app:user_login_to')

    # Hacemos un get_queryset para definir la lista
    def get_queryset(self):
        # Le pasamos como parametros el usuario para hacer la consulta
        # El parametro self.request.user nos traen el usuario que esta ectivo en sesrion
        return Favorites.objects.entradas_user(self.request.user)

class AddFavoritosView(View):

    def post(self, reques, *args, **kwargs):
        # Recuperamos un usuario
        usuario = self.reques.user
        # Recuperamos el id de la endrada
        entrada = entry.objects.get(id=self.kwargs['pk'])
        # Registramos favorito
        Favorites.objects.create(
            user = usuario,
            entry = entrada,
        )

        return HttpResponseRedirect