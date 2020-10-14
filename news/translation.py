from modeltranslation.translator import TranslationOptions, translator, register

from .models import News, Tag


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'author')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title', )
