from .models import Privilege
import django_filters


class PilgaFilter(django_filters.FilterSet):
    class Meta:
        model = Privilege
        fields = ['title', 'privilege_type', 'group', 'subgroup', 'region', 'document_type']