from django.db import models
from django.conf import settings

# Apps de terceros
from model_utils.models import TimeStampedModel
#
from applications.entrada.models import Entry
# From managers
from .managers import FavoriteManager


class Favorites(TimeStampedModel):
    """Model definition for Favorites."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )
    objects = FavoriteManager()

    class Meta:
        """Meta definition for Favorites."""

        verbose_name = 'Favorites'
        verbose_name_plural = 'Favorites'
        # Se usa este campo para que un usuario no pueda
        # registrar varias veces una entrada como favorita
        unique_together = ('user', 'entry')

    def __str__(self):
        return self.entry.title
