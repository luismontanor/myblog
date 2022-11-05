from django import forms

# From models
from .models import Suscriber, Contact


class SuscriberForm(forms.ModelForm):
    """Form definition for Suscriber."""

    class Meta:
        """Meta definition for Suscriberform."""

        model = Suscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico...',
                }
            ),
        }

# Degfinicion de formulario para el footer -> Formulario de contacto
class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('__all__')
