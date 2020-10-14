from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from filer.fields.image import FilerImageField

# Create your models here.


class Slider(models.Model):
    description = RichTextUploadingField(blank=True, null=True, max_length=2048, verbose_name='Текст для слайдера')
    image = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE, related_name='slider_images')

    def __str__(self):
        return 'Изображения слайдера'

    class Meta:
        verbose_name = 'Изображения слайдера'
        verbose_name_plural = 'Изображения слайдера'


class PrivilegeType(models.Model):
    type = models.CharField(max_length=500, null=True, blank=True, verbose_name='Тип')

    def __str__(self):
        return '{}'.format(self.type)

    class Meta:
        verbose_name = 'Тип льготы/субсидии'
        verbose_name_plural = 'Тип льготы/субсидии'


class Group(models.Model):
    group = models.CharField(max_length=500, null=True, blank=True, verbose_name='Группа льгот/субсидий (уровень 1)')

    def __str__(self):
        return '{}'.format(self.group)

    class Meta:
        verbose_name = 'Группа льгот/субсидий (уровень 1)'
        verbose_name_plural = 'Группа льгот/субсидий (уровень 1)'


class SubGroup(models.Model):
    group = models.CharField(max_length=500, null=True, blank=True, verbose_name='Подгруппа льгот/субсидий (уровень 2)')

    def __str__(self):
        return '{}'.format(self.group)

    class Meta:
        verbose_name = 'Группа льгот/субсидий (уровень 2)'
        verbose_name_plural = 'Группа льгот/субсидий (уровень 2)'


class Region(models.Model):
    region = models.CharField(max_length=500, null=True, blank=True, verbose_name='Регион')

    def __str__(self):
        return '{}'.format(self.region)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регион'


class DocumentType(models.Model):
    document = models.CharField(max_length=500, null=True, blank=True, verbose_name='Тип документа')

    def __str__(self):
        return '{}'.format(self.document)

    class Meta:
        verbose_name = 'Тип нормативного документа'
        verbose_name_plural = 'Тип нормативного документа'


class IssuedBy(models.Model):
    issued = models.CharField(max_length=500, null=True, blank=True, verbose_name='Кем выдан')

    def __str__(self):
        return '{}'.format(self.issued)

    class Meta:
        verbose_name = 'Кем выдан'
        verbose_name_plural = 'Кем выдан'


class Agency(models.Model):
    agency = models.CharField(max_length=500, null=True, blank=True, verbose_name='Орган рассмотрения выдачи льготы/субсидии')
    building = models.CharField(max_length=500, null=True, blank=True, verbose_name='Учреждение')
    activity = RichTextUploadingField(null=True, blank=True, verbose_name='Деятельность')
    image = FilerImageField(null=True, blank=True, verbose_name='Изображение', on_delete=models.CASCADE, related_name='agency_image')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Адрес')
    department = models.CharField(max_length=50, null=True, blank=True, verbose_name='Департамент')
    work_time = models.CharField(max_length=50, null=True, blank=True, verbose_name='Режим работы')
    contact_person = models.CharField(max_length=50, null=True, blank=True, verbose_name='Контактное лицо')
    contact_phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Контакты тел.')
    geo_lat = models.CharField(max_length=50, null=True, blank=True, verbose_name='широта')
    geo_long = models.CharField(max_length=50, null=True, blank=True, verbose_name='долгота')

    def __str__(self):
        return '{}'.format(self.agency)

    class Meta:
        verbose_name = 'Орган рассмотрения выдачи льготы/субсидии'
        verbose_name_plural = 'Орган рассмотрения выдачи льготы/субсидии'


class RequiredDocument(models.Model):
    required_document = models.CharField(max_length=500, null=True, blank=True, verbose_name='Требуемые документы')

    def __str__(self):
        return '{}'.format(self.required_document)

    class Meta:
        verbose_name = 'Требуемые документы'
        verbose_name_plural = 'Требуемые документы'


class Privilege(models.Model):
    privilege_type = models.ForeignKey(PrivilegeType, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_type')
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_group',
                                  verbose_name='Группа льгот/субсидий (уровень 1)')
    subgroup = models.ForeignKey(SubGroup, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_subgroup',
                                  verbose_name='Группа льгот/субсидий (уровень 2)')
    national = models.BooleanField(default=False, null=True, blank=True, verbose_name='Общенациональный (Да/Нет)')
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_region',
                               verbose_name='Регион')
    title = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Название льготы/субсидии')
    document_type = models.ForeignKey(DocumentType, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_document_type',
                               verbose_name='Тип нормативного документа')
    number = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Номер нормативного документа')
    date = models.DateField(auto_now=True, verbose_name='Дата нормативного документа')
    issued = models.ForeignKey(IssuedBy, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_issued',
                                      verbose_name='Кем выдан')
    slug = models.CharField(max_length=1000, null=True, blank=True, verbose_name='WEB Ссылка на официальный источник')
    value = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Сумма или значение льготы/ субсидии')
    duration_start = models.CharField(max_length=100, null=True, blank=True, verbose_name='Срок действия льготы/субсидии от')
    duration_end = models.CharField(max_length=100, null=True, blank=True, verbose_name='Срок действия льготоы/субсидии до')
    single_pay = models.BooleanField(default=False, null=True, blank=True, verbose_name='Одноразовая выплата (Да/Нет)')
    period_start = models.CharField(max_length=100, null=True, blank=True,
                                    verbose_name='Период выплаты с')
    period_end = models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name='Период выплаты до')
    agency = models.ForeignKey(Agency, null=True, blank=True, on_delete=models.CASCADE, related_name='privilege_agency',
                                  verbose_name='Орган рассмотрения выдачи льготы/субсидии')
    annual_revision = models.BooleanField(default=False, null=True, blank=True, verbose_name='Ежегодный пересмотр (Да/Нет)')
    period_revision = models.CharField(max_length=100, null=True, blank=True,
                                    verbose_name='Период/Месяц пересмотра')
    required_document = models.ManyToManyField(RequiredDocument, blank=True, related_name='privilege_required_document',
                               verbose_name='Требуемые документы')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return 'Льгота'

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'


class About(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True, verbose_name='О проекте')
    description = RichTextUploadingField(null=True, blank=True, verbose_name='Оптисание проекта')
    image = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE, related_name='about_image')
    geo_lat = models.CharField(max_length=50, null=True, blank=True, verbose_name='широта')
    geo_long = models.CharField(max_length=50, null=True, blank=True, verbose_name='долгота')

    def __str__(self):
        return 'О проекте'

    class Meta:
        verbose_name = 'О проекте'
        verbose_name_plural = 'О проекте'


class FeedBack(models.Model):
    fio = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Имя и Фамилия')
    message = RichTextUploadingField(null=True, blank=True, verbose_name='Сообщение')
    theme = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Тема сообщения')
    phone = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Контактный телефон')
    email = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Email')

    def __str__(self):
        return 'Обратная связь'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Subscribe(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return 'Подписка'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'
