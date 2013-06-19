from adijux.views import SwitchLanguage, FrontView, GalleryView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from adijux import settings
from pages.views import PageView
from room.views import RoomsView, RoomView, BookingView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^switch-language/', SwitchLanguage.as_view(), name='switch-language'),
    url(r'^booking/$', BookingView.as_view(), name='booking'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^rooms/$', RoomsView.as_view(), name='rooms'),
    url(r'^rooms/(?P<id>[0-9A-Za-z-_.//]+)/$', RoomView.as_view(slug_field='id'), name='room'),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', PageView.as_view(slug_field='url'), name='page'),
    url(r'^$', FrontView.as_view(), name='front'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
