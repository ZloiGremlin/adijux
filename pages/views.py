from django.views.generic import DetailView, TemplateView
from models import Page

class PageView(DetailView):
    template_name = 'pages/page-detail.html'
    model = Page
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        ctx = super(PageView, self).get_context_data(**kwargs)
        l = self.request.session.get('lang','ru')
        return ctx
