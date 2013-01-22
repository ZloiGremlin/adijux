# vim:fileencoding=utf-8
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from django.db.models import permalink

class Page(TranslatableModel):
    class Meta(object):
        verbose_name=u'Страница'
        verbose_name_plural=u'Страницы'


    translations = TranslatedFields(
        name = models.CharField(verbose_name=u'Название страницы', max_length=255),
        menu = models.CharField(verbose_name=u'Название в меню', max_length=255, blank=True, null=True),
        text = models.TextField(verbose_name=u'Текст', blank=True, null=True),
        title = models.TextField(verbose_name=u'Тайтл', null=True, blank=True),
        meta_keywords = models.TextField(verbose_name=u'Keywords', null=True, blank=True),
        meta_description = models.TextField(verbose_name=u'Description', null=True, blank=True),
    )

    url = models.CharField(max_length=255, verbose_name=u'Адрес(URL)', unique=True)
    front = models.BooleanField(default=False, verbose_name=u'Главная страница')


    def __unicode__(self):
        return self.lazy_translation_getter('name', 'Id: %s' % self.pk)

    @permalink
    def get_absolute_url(self):
        return 'page', (self.url,), {}


class Block(TranslatableModel):
    class Meta(object):
        verbose_name=u'Блок'
        verbose_name_plural=u'Блоки'

    name = models.CharField(verbose_name=u'Машинное имя', max_length=255, help_text=u'Только на латинице')

    translations = TranslatedFields(
        text = models.TextField(verbose_name=u'Код', blank=True, null=True),
    )

    def __unicode__(self):
        return self.name


class Menu(TranslatableModel):
    class Meta(object):
        verbose_name=u'Меню'
        verbose_name_plural=u'Меню'
        ordering = ['sort']


    translations = TranslatedFields(
        name = models.CharField(verbose_name=u'Название пункта', max_length=255)
    )

    position = models.CharField(verbose_name=u'Положение', default='top', max_length=255)
    url = models.CharField(verbose_name=u'URL', max_length=255, blank=True, null=True)
    page = models.ForeignKey(Page, related_name='menus', blank=True, null=True, verbose_name=u'Страница')
    parent = models.ForeignKey('self', verbose_name=u'Родительский пункт', blank=True, null=True, related_name='children')
    sort = models.IntegerField(default=10, verbose_name=u'Приоритет')


    def __unicode__(self):
        return self.lazy_translation_getter('name', 'Id: %s' % self.pk)