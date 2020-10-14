from django.utils.translation import ugettext_lazy, get_language
# from allauth.socialaccount import providers
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.urls import translate_url, reverse
from django.utils import timezone
# from django.template import defaulttags
from django.template.defaultfilters import date

from jinja2.environment import Environment
from jinja2.runtime import Undefined

from easy_thumbnails.templatetags.thumbnail import thumbnail_url

from .extensions import (now, format_date, pagination, page_title_pagination)


class SilentUndefined(Undefined):
    """ Класс, который реализует обработку не существующих значений аналогично шаблонизатору Django"""

    def _fail_with_undefined_error(self, *args, **kwargs):
        class EmptyString(str):
            def __call__(self, *args, **kwargs):
                return ''

        return EmptyString()

    __add__ = __radd__ = __mul__ = __rmul__ = __div__ = __rdiv__ = \
        __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = \
        __mod__ = __rmod__ = __pos__ = __neg__ = __call__ = \
        __getitem__ = __lt__ = __le__ = __gt__ = __ge__ = __int__ = \
        __float__ = __complex__ = __pow__ = __rpow__ = \
        _fail_with_undefined_error


class JinjaEnvironment(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.undefined = SilentUndefined

        self.globals.update(
            {
                'type': type,
                'len': len,
                'int': int,
                'str': str,
                '_': ugettext_lazy,
                'settings': settings,
                'static': staticfiles_storage.url,
                'url': reverse,
                'format_date': format_date,
                'get_language': get_language,
                'now': now,
                'comparable_now': timezone.now,
                'thumbnail_url': thumbnail_url,
                'translate_url': translate_url,
                # 'insert_file_content': insert_file_content,
                # 'check_icon': check_icon,
                # 'with': defaulttags.do_with
                'locale_date_formatter': date,
                'pagination': pagination,
                # 'provider_login_url': provider_login_url,
                # 'shared_session': shared_session,
                'page_title_pagination': page_title_pagination,
                # 'z_encode': z_encode,
            }
        )
        self.filters.update()
