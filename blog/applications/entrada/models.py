# standard library
from datetime import timedelta, datetime

#
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Apps de terceross.
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# From managers
from .managers import EntryManager


# Heredamos del TimeStampedModel
class Category(TimeStampedModel):
    """Model definition for Category."""

    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30,
        unique=True
    )

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


# Heredamos del TimeStampedModel
class Tag(TimeStampedModel):
    """Model definition for Tag."""

    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


# Heredamos del TimeStampedModel
class Entry(TimeStampedModel):
    """Model definition for Entry."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField(
        'Resumen',
        max_length=200
    )
    content = RichTextUploadingField()
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen',
        upload_to='Entry',
        height_field=None,
        width_field=None,
        max_length=None
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    # El atributo slug es obigatorio para trabajar en el posicionamiento web
    # Y generar urls de forma automatica
    slug = models.SlugField(editable=False, max_length=300)

    # Importamos nuestros managers
    objects = EntryManager()

    class Meta:
        """Meta definition for Entry."""

        verbose_name = 'Entry'
        verbose_name_plural = 'Entrys'

    def __str__(self):
        return self.title

    # De esta manera se crea un url slug
    def save(self, *args, **kwargs):
        # Calculamos el total de segundos en la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)
