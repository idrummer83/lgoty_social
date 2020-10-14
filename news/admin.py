from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import News, NewsImage, Tag


class ImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    verbose_name = "Изображения"
    verbose_name_plural = "Изображения"


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'main_page', 'created_at', 'updated_at', 'published', 'author')
    inlines = (ImageInline,)


@admin.register(Tag)
class PTagAdmin(TranslationAdmin):
    list_display = ('id', 'title')
