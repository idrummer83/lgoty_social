import logging
import re
import random
import string
# import simplejson
import time
from html import unescape
from collections import OrderedDict
from math import ceil

from django.apps import apps
from django.conf import settings
from django.db.models import Q, Sum, Case, FloatField, When
from django.http.response import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.urls import reverse
from django.utils.formats import localize
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

from easy_thumbnails.files import get_thumbnailer
from filer.models import Image


def get_logger(name):
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    if settings.DEBUG:
        ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] | %(name)s | [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


log = get_logger(__name__)


def gen_random_pass(length=8):
    return ''.join(random.choice(
        string.ascii_lowercase + string.digits) for _ in range(length))


def transliterate(string):
    tr = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'yi',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ь': '',
        'ы': 'y',
        'э': 'ye',
        'ю': 'yu',
        'я': 'ya',
    }

    return ''.join([tr.get(c, c) for c in string.lower()])


def slugify(string):
    string = transliterate(string)
    st = re.sub(r'\W', '-', string)
    st = re.sub(r'-{2,}', '-', st)
    st = re.sub(r'(^-|-$)', '', st)
    return st


# def captcha_word():
#     #TODO: optimize
#     from reikartz.models import CaptchaDictionary       # avoiding circular imports
#     selected_word = random.choice([*CaptchaDictionary.objects.values_list('word', flat=True)]).lower()
#     return (
#         (selected_word, selected_word)
#     )


# def check_form_captcha(func):
#     from reikartz.forms import CaptchaForm
#     def inner(request, *args, **kwargs):
#         human = False
#         form = CaptchaForm(request.POST)
#
#         if request.session.get('captcha_count', settings.MAXIMUM_SUCCESS_CAPTCHA) < settings.MAXIMUM_SUCCESS_CAPTCHA:
#             human = True
#             request.session['captcha_count'] += 1
#
#         if form.is_valid():
#             human = True
#             request.session['captcha_count'] = 0
#
#         if human:
#             return func(request, *args, **kwargs)
#
#         return JsonResponse({'captcha': 'error'})
#         # return JsonResponse({'captcha': 'fail'})
#     return inner


def format_date(date, datetime_format=None):
    if isinstance(datetime_format, int):
        datetime_format = settings.DATETIME_FORMATS.get(datetime_format)

    if isinstance(date, str):
        date = parse_datetime(date)

    date = timezone.localtime(date)

    if datetime_format:
        return date.strftime(datetime_format)

    return localize(date)


def clean_html(raw_html):
    return unescape(re.sub(re.compile('<.*?>'), '', raw_html))


def iso_8601_date_format(datetime):
    return datetime.astimezone().replace(microsecond=0).isoformat()
