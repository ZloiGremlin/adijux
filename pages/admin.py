# vim:fileencoding=utf-8

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from mptt.admin import MPTTModelAdmin
from models import Page, Block, Menu

class PageAdmin(TranslatableAdmin):
    list_display = ['__unicode__', 'url']

admin.site.register(Page, PageAdmin)
admin.site.register(Block, TranslatableAdmin)
admin.site.register(Menu, TranslatableAdmin)
