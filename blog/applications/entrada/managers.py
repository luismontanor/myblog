from django.db import models


class EntryManager(models.Manager):
    """Procedimientos para entrada"""

    # Creamos una consulta para entrada
    def entrada_en_portada(self):
        # Hacemos un return de un filter
        return self.filter(
            # Filtramos aquellos que tengan el atributo public igual a True
            public=True,
            # Filtramos aquellos que tengan portada igual a True
            portada=True,
        ).order_by('-created').first()

    # Creamos una consulta para varias entradas en home
    def entradas_en_home(self):
        # Devolvemos las ultimas 4 entradas
        return self.filter(
            # Filtramos aquellos que tengan el atributo public igual a True
            public=True,
            # Filtramos aquellos que tengan el atributo in_home igual a True
            in_home=True
        ).order_by('-created')[:4]

    # Creamos una consulta para ver los articulos recientes
    def entradas_recientes(self):
        # Devolvemos las 6 entradas recientes entradas
        return self.filter(
            # Filtramos aquellos que tengan el atributo public igual a True
            public=True,
        ).order_by('-created')[:6]

    def buscar_entrada(self, kword, categoria):
        # Procedimientos para buscar entradas por categoria y palabra claves
        # Valindamos que hayan categorias
        if len(categoria) > 0:
            return self.filter(
                # Filtramos en base al campo shor_name de el modelo Category
                category__short_name=categoria,
                # Filtramos en base al campo title de el modelo Entry
                title__icontains=kword,
                # Filtramos todos aquellas entradas que tengan el campo public marcado con True
                public=True
                # Por ultimo los ordenamos segun su fecha de creacion
            ).order_by('-created')
        # En caso no se haya proporcionado una categoria se filtra omitiendo este campo
        else:
            return self.filter(
                # Filtramos en base al campo title de el modelo Entry
                title__icontains=kword,
                # Filtramos todos aquellas entradas que tengan el campo public marcado con True
                public=True
                # Por ultimo los ordenamos segun su fecha de creacion
            ).order_by('-created')