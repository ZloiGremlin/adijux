# vim:fileencoding=utf-8
from django.views.generic import TemplateView
from models import Room

class RoomsView(TemplateView):
    template_name = 'room/list.html'

    def get_context_data(self, **kwargs):
        ctx = super(RoomsView, self).get_context_data(**kwargs)
        ctx['rooms'] = Room.objects.all()
        ctx['menuname'] = u'Номера'
        return ctx