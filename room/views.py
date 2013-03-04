# vim:fileencoding=utf-8
from django.views.generic import TemplateView, DetailView
from models import Room

class RoomsView(TemplateView):
    template_name = 'room/list.html'

    def get_context_data(self, **kwargs):
        ctx = super(RoomsView, self).get_context_data(**kwargs)
        ctx['rooms'] = Room.objects.all()
        ctx['menuname'] = u'Номера'
        return ctx

class RoomView(DetailView):
    template_name = 'room/detail.html'
    context_object_name = 'room'
    slug_url_kwarg = 'id'
    model = Room

    def get_context_data(self, **kwargs):
        ctx = super(RoomView, self).get_context_data(**kwargs)
        ctx['rooms'] = Room.objects.all()
        ctx['menuname'] = u'Номера'
        return ctx