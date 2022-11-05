from django.db import models

# Apps de terceros
from model_utils.models import TimeStampedModel


# Heredamos del TimeStampedModel
class Home(TimeStampedModel):
    """Model definition for Home."""

    titulo = models.CharField(
        'Nombre',
        max_length=50
    )
    description = models.TextField()
    about_title = models.TextField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto', max_length=254,
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono de contacto',
        max_length=20
    )


    class Meta:
        """Meta definition for Home."""

        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

    def __str__(self):
        return self.titulo


class Suscriber(TimeStampedModel):
    """Model definition for Suscriber."""

    email = models.EmailField()

    class Meta:
        """Meta definition for Suscriber."""

        verbose_name = 'Suscriber'
        verbose_name_plural = 'Suscribers'

    def __str__(self):
        return self.email


class Contact(models.Model):
    """Model definition for Contact."""

    full_name = models.CharField(
        'Nombre',
        max_length=50
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name


