from modeltranslation.translator import TranslationOptions, translator, register

from .models import Slider, Privilege, PrivilegeType, Group, SubGroup, Region, DocumentType, IssuedBy, Agency,\
    RequiredDocument, About, FeedBack, Subscribe


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(Privilege)
class PrivilegeTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(PrivilegeType)
class PrivilegeTypeTranslationOptions(TranslationOptions):
    fields = ('type', )


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('group', )


@register(SubGroup)
class SubGroupTranslationOptions(TranslationOptions):
    fields = ('group', )


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region', )


@register(DocumentType)
class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('document', )


@register(IssuedBy)
class IssuedByTranslationOptions(TranslationOptions):
    fields = ('issued', )


@register(Agency)
class AgencyTranslationOptions(TranslationOptions):
    fields = ('agency', )


@register(RequiredDocument)
class RequiredDocumentTranslationOptions(TranslationOptions):
    fields = ('required_document', )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(FeedBack)
class FeedBackTranslationOptions(TranslationOptions):
    fields = ()


@register(Subscribe)
class SubscribeTranslationOptions(TranslationOptions):
    fields = ()
