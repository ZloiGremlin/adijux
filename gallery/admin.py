# vim:fileencoding=utf-8

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from mptt.admin import MPTTModelAdmin
from models import ImageElement


admin.site.register(ImageElement, TranslatableAdmin)