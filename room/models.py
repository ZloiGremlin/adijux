# vim:fileencoding=utf-8
from datetime import timedelta
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
        verbose_name = u'Номер'
        verbose_name_plural = u'Номера'

    translations = TranslatedFields(
        name=models.CharField(verbose_name=u'Название номера', max_length=255),
        text=models.TextField(verbose_name=u'Текст', blank=True, null=True),
    )

    @permalink
    def get_absolute_url(self):
        return 'room', (self.id,), {}

    def __unicode__(self):
        return self.lazy_translation_getter('name', 'Id: %s' % self.pk)

    def get_image(self):
        return self.images.all()[0].image

    def get_dates(self):
        dates = []
        for date in self.dates.all():
            if date.date_from == date.date_to:
                dates.append(date.date_from)
            else:
                future = date.date_to
                while date.date_from != future:
                    dates.append(future)
                    future = future - timedelta(days=1)
                dates.append(date.date_from)
        return dates


class RoomImages(models.Model):
    class Meta(object):
        verbose_name = u'Фото номера'
        verbose_name_plural = u'Фото номера'

    room = models.ForeignKey(Room, related_name='images')
    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение')


class RoomDates(models.Model):
    class Meta(object):
        verbose_name = u'Закрытые даты'
        verbose_name_plural = u'Закрытые даты'

    room = models.ForeignKey(Room, related_name='dates')
    date_from = models.DateField(verbose_name=u'Дата от')
    date_to = models.DateField(verbose_name=u'Дата до')


BEDS = (
    ('div', u'Раздельные'),
    ('two', u'Двуспальные')
)

WINDOW = (
    ('tower', u'Башня'),
    ('rock', u'Холмы')
)


class RoomBooking(models.Model):
    class Meta(object):
        verbose_name = u'Бронь'
        verbose_name_plural = u'Бронь'

    name = models.CharField(verbose_name=u'Имя', max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=255, blank=True, null=True)
    email = models.CharField(verbose_name=u'E-mail', max_length=255, blank=True, null=True)
    room = models.ForeignKey(Room, related_name='booking', verbose_name=u'Тип номера')
    people = models.CharField(verbose_name=u'Количество человек', max_length=255, blank=True, null=True)
    qty = models.CharField(verbose_name=u'Количество номеров', max_length=255, blank=True, null=True)
    date = models.CharField(verbose_name=u'Дата', max_length=255, blank=True, null=True)
    bed = models.CharField(verbose_name=u'Кровати', max_length=255, blank=True, null=True, choices=BEDS)
    place = models.BooleanField(verbose_name=u'Дополнительное место', default=False)
    window = models.CharField(verbose_name=u'Вид из окна', max_length=255, blank=True, null=True, choices=WINDOW)
    cart = models.BooleanField(verbose_name=u'Карта постоянного клиента', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата отправки', blank=True, null=True)


    def __unicode__(self):
        return self.name