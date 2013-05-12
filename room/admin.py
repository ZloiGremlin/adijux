# vim:fileencoding=utf-8

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from models import Room, RoomImages, RoomDates, RoomBooking

class RoomImageInline(admin.TabularInline):
    model = RoomImages
    extra = 1

class RoomDateInline(admin.TabularInline):
    model = RoomDates
    extra = 3

class RoomAdmin(TranslatableAdmin):
    inlines = [RoomImageInline, RoomDateInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomBooking, BookAdmin)
