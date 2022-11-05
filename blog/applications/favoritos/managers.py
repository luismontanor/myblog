from django.db import models


class FavoriteManager(models.Manager):

    # Manager para consultar las entradas marcadas como favoritas de un usuario
    def entradas_user(self, usuario):
        return self.filter(
            # Filtramos todasl las entradas que tengan public igual a True
            entry__public=True,
            # Filtramos segun el usuario que recuperamos de las vistas
            user=usuario
            # Ordenamos cronologicamente de forma descendente
        ).order_by("-created")