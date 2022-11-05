# From models Home
from applications.home.models import Home


# Procesor para recuperar telefono y correo del registro home
# Esta es la estructura que debemos seguir si queremos escribir un procesor
def home_contact(request):
    # Recuperamos el ultimo registro creado del modelo Home
    home = Home.objects.latest('created')

    # Para retornar un processor devolvemos un diccionario
    return{
        'phone': home.phone,
        'contact_email': home.contact_email,
    }