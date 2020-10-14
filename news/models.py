from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок тега')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок новости")
    description = RichTextUploadingField(verbose_name="Новость")
    slug = models.SlugField(verbose_name='Slug', max_length=200, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=False)
    main_page = models.BooleanField(verbose_name='Главная страница', default=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги', related_name='news_tags')
    author = models.CharField(max_length=500, null=True, verbose_name="Автор новости")
    video_slug = models.CharField(max_length=2000, null=True, blank=True, verbose_name="ССылка на видео")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость', related_name='news_images')
    image = FilerImageField(
        verbose_name='Изображение',
        on_delete=models.CASCADE,
        related_name='news_images'
    )
    is_main = models.BooleanField(
        verbose_name='Главное изображение',
        default=False
    )

    def __str__(self):
        return '%s' % (self.news.title)

    class Meta:
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новости'
