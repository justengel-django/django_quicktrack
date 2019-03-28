import django_filters
from django_filters.widgets import RangeWidget
from taggit.models import Tag

from .models import TrackType, TrackRecord


def get_types(request):
    if request is None:
        return TrackType.objects.none()
    return TrackType.objects.with_user(request.user)


def get_tags(request):
    if request is None:
        return []
    return Tag.objects.all()


class TrackingFilter(django_filters.FilterSet):
    type = django_filters.ModelChoiceFilter(queryset=get_types)
    date = django_filters.DateFromToRangeFilter(field_name='date', widget=RangeWidget(attrs={'type': 'date'}))
    tags = django_filters.ModelChoiceFilter(queryset=get_tags)

    class Meta:
        model = TrackRecord
        fields = ['type', 'date', 'tags']
