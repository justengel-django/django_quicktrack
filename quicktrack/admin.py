from django.contrib import admin
from taggit_helpers.admin import TaggitListFilter
from .models import TrackType, TrackRecord, QuickAction


@admin.register(TrackType)
class TrackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'member_names')
    search_fields = ('owner', 'name')
    list_filter = ('owner', 'name')


@admin.register(TrackRecord)
class TrackRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'description', 'date', 'tag_list')
    search_fields = ('user', 'type', 'description')
    list_filter = ('user', 'type', 'date', TaggitListFilter)

    def get_queryset(self, request):
        return super(TrackRecordAdmin, self).get_queryset(request).prefetch_related('tags')


@admin.register(QuickAction)
class QuickActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'description', 'tags')
    search_fields = ('user', 'type', 'description')
    list_filter = ('user', 'type')
