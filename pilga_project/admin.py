from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

# Register your models here.

from .models import Slider, Privilege, PrivilegeType, Group, SubGroup, Region, DocumentType, IssuedBy, Agency, \
    RequiredDocument, About, FeedBack, Subscribe


@admin.register(PrivilegeType)
class PrivilegeTypeAdmin(TranslationAdmin):
    list_display = ('id', 'type')


@admin.register(Group)
class GroupAdmin(TranslationAdmin):
    list_display = ('id', 'group')


@admin.register(SubGroup)
class SubGroupAdmin(TranslationAdmin):
    list_display = ('id', 'group')


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ('id', 'region')


@admin.register(DocumentType)
class DocumentTypeAdmin(TranslationAdmin):
    list_display = ('id', 'document')


@admin.register(IssuedBy)
class IssuedByAdmin(TranslationAdmin):
    list_display = ('id', 'issued')


@admin.register(Agency)
class AgencyAdmin(TranslationAdmin):
    list_display = ('id', 'agency')


@admin.register(RequiredDocument)
class RequiredDocumentAdmin(TranslationAdmin):
    list_display = ('id', 'required_document')


@admin.register(Privilege)
class PrivilegeAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'privilege_type', 'group', 'subgroup', 'region', 'document_type', 'issued', 'agency')


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ('id', 'description')


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'title')


@admin.register(FeedBack)
class FeedBackAdmin(TranslationAdmin):
    list_display = ('id', 'fio', 'message', 'theme', 'phone', 'email')


@admin.register(Subscribe)
class FeedBackAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'phone', 'email')
