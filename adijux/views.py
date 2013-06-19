# vim:fileencoding=utf-8
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from pages.models import Page, Menu
from gallery.models import ImageElement, Album


class SwitchLanguage(TemplateView):
    def get(self, request, *args, **kwargs):
        lang = request.GET.get('language', None)
        if lang:
            request.session['lang'] = lang
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class FrontView(TemplateView):
    template_name = 'front.html'

    def get_context_data(self, **kwargs):
        ctx = super(FrontView, self).get_context_data(**kwargs)
        ctx['object'] = Page.objects.get(front=True)
        ctx['menu'] = Menu.objects.filter(parent=None, position='front')
        ctx['gallery'] = ImageElement.objects.all().order_by('?')[:6]
        return ctx


class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(GalleryView, self).get_context_data(**kwargs)
        ctx['menuname'] = u'Галерея'
        ctx['gallery'] = Album.objects.filter(gallery=True)
        return ctx