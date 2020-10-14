import zlib
from base64 import b64encode, b64decode

from django.utils import timezone
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from datetime import datetime

from pilga.utils import format_date

# def reverse_url(*args, **kwargs):
#     return reverse(args[0], args=args[1:], kwargs=kwargs)

moths_dict = {
    1: ' января', 2: ' февраля', 3: ' марта', 4: ' апреля', 5: ' мая', 6: ' июня',
    7: ' июля', 8: ' августа', 9: ' сентября', 10: ' октября', 11: ' ноября', 12: ' декабря',
}


def nearest_date_format(str_date):
    date = datetime.strptime(str_date, "%Y-%m-%d")
    day_text = str(date.day)
    month_text = moths_dict[date.month]
    return 'c ' + day_text + month_text if day_text != '2' else 'cо ' + day_text + month_text


def now(datetime_format=None):
    return format_date(timezone.now(), datetime_format)


def insert_file_content(file):
    try:
        file_handler = file.read()
        if type(file_handler) == str:
            content = file_handler
        else:
            content = file_handler.decode("utf-8")
        file.seek(0)
    except:
        print(file)
        content = ''
    return content


def pagination(paginator, page):
    page_range = list(paginator.page_range)
    page_range_len = len(page_range)
    if page_range_len > 6:
        page_num = page.number
        page_index = page_range.index(page_num)
        # Если текущий элемент находится дальше чем на 6 элементов с конца или начала, выводим элипсис
        ellipsis_start = ['...'] if page_index > 5 else []
        ellipsis_end = ['...'] if page_range_len - page_index > 6 else []
        # Заменяем середину списка страниц, на те, которые будут в зоне видимости
        middle = page_range[max(page_num - 3, 3):min(page_num + 2, page_range[-4])]
        page_range[3:-3] = ellipsis_start + middle + ellipsis_end

    return format_html(render_to_string(
        'pilga_project/pagination.html',
        {'page': page, 'page_range': page_range}
    ))


def page_title_pagination(title, page_number):
    if page_number != 1:
        return '{} ({}{})'.format(title, _('стр.'), page_number)
    return title


def z_encode(text):
    return b64encode(zlib.compress(text.encode('utf-8'))).decode('utf-8')


def z_decode(text):
    return zlib.decompress(b64decode(text)).decode('utf-8')
