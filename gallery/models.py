# vim:fileencoding=utf-8
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from django.db.models import permalink
import os
import uuid
from adijux import settings
from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.shortcuts import get_thumbnail
from django.utils import translation


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(getattr(settings, 'PRODUCT_IMAGE_UPLOAD_TO', 'catalog/'), filename)

class ImageElement(TranslatableModel):
    class Meta(object):
        verbose_name=u'Изображение'
        verbose_name_plural=u'Изображения'

    translations = TranslatedFields(
        name = models.CharField(verbose_name=u'Название изображения', max_length=255),
    )

    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение')

    def __unicode__(self):
        return self.lazy_translation_getter('name', 'Id: %s' % self.pk)

