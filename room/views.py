# vim:fileencoding=utf-8
import datetime
from django import forms
from django.views.generic import TemplateView, DetailView, FormView
from models import Room, RoomBooking


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


class BookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking


class BookingView(FormView):
    template_name = 'room/booking.html'
    form_class = BookingForm
    success_url = '/success/'

    def get_initial(self):
        initial = {
            'room': None,
            'qty': u'1 номер',
            'people': u'2 человека',
            'date': datetime.date.today().strftime('%d-%m-%Y')
        }
        if self.request.GET.get('room', False):
            room = Room.objects.get(id=int(self.request.GET.get('room')))
            initial['room'] = room
        return initial

    def get_context_data(self, **kwargs):
        ctx = super(BookingView, self).get_context_data(**kwargs)
        ctx['rooms'] = Room.objects.all()
        ctx['object'] = None
        if self.request.GET.get('room', False):
            ctx['room'] = Room.objects.get(id=int(self.request.GET.get('room')))
        ctx['menuname'] = u'Бронирование'
        return ctx

    def form_valid(self, form):
        o = form.save()
        return super(BookingView, self).form_valid(form)