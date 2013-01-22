from django.utils import translation


class Language(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        lang_code = request.session.get('lang', None)
        if not lang_code:
            lang_code = 'ru'
        request.session['lang'] = lang_code
        translation.activate(lang_code)
