# vim:fileencoding=utf-8
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from django.db.models import permalink
import os
import uuid
from adijux import settings
from sorl.thumbnail.fields import ImageField


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(getattr(settings, 'PRODUCT_IMAGE_UPLOAD_TO', 'catalog/'), filename)

class Room(TranslatableModel):
    class Meta(object):
        verbose_name=u'Номер'
        verbose_name_plural=u'Номера'

    translations = TranslatedFields(
        name = models.CharField(verbose_name=u'Название номера', max_length=255),
    )

    def __unicode__(self):
        return self.lazy_translation_getter('name', 'Id: %s' % self.pk)

    def get_image(self):
        return self.images.all()[0].image

class RoomImages(models.Model):
    class Meta(object):
        verbose_name=u'Фото номера'
        verbose_name_plural=u'Фото номера'

    room = models.ForeignKey(Room, related_name='images')
    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение')

