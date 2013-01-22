# vim:fileencoding=utf-8

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from mptt.admin import MPTTModelAdmin
from models import Room, RoomImages

class RoomImageInline(admin.TabularInline):
    model = RoomImages
    extra = 1

class RoomAdmin(TranslatableAdmin):
    inlines = [RoomImageInline]


admin.site.register(Room, RoomAdmin)
