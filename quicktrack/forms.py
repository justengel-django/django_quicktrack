from django import forms
from django.db.models import Q

from .models import TrackType, TrackRecord, QuickAction


__all__ = ['DeleteForm', 'TrackRecordForm', 'TrackTypeForm', 'QuickActionForm']


class DeleteForm(forms.Form):
    pk = forms.IntegerField(required=True, widget=forms.HiddenInput())


class TrackRecordForm(forms.ModelForm):
    class Meta:
        model = TrackRecord
        fields = ['user', 'type', 'description', 'tags']
        widgets = {
            'user': forms.HiddenInput(),
            }

    def __init__(self, *args, **kwargs):
        super(TrackRecordForm, self).__init__(*args, **kwargs)
        try:
            self.fields['type'].queryset = TrackType.objects.with_user(self.fields['user'].queryset[0])
        except (IndexError, Exception):
            pass


class TrackTypeForm(forms.ModelForm):
    class Meta:
        model = TrackType
        fields = ['name', 'owner', 'members']
        widgets = {
            'owner': forms.HiddenInput(),
            }


class QuickActionForm(forms.ModelForm):
    class Meta:
        model = QuickAction
        fields = ['name', 'color', 'icon', 'user', 'type', 'description', 'tags']
        widgets = {
            'user': forms.HiddenInput(),
            }

    def __init__(self, *args, **kwargs):
        super(QuickActionForm, self).__init__(*args, **kwargs)
        try:
            self.fields['type'].queryset = TrackType.objects.with_user(self.fields['user'].queryset[0])
        except (IndexError, Exception):
            pass
