from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager


class TrackTypeManager(models.Manager):
    def with_user(self, user):
        qs = self.get_queryset()
        if self.model == TrackType:
            qs = qs.filter(Q(owner=user) | Q(members__in=[user])).distinct()
        elif self.model == TrackRecord:
            qs = qs.filter(Q(type__owner=user) | Q(type__members__in=[user])).distinct()
        return qs


class TrackType(models.Model):
    objects = TrackTypeManager()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='track_types')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='track_records')
    name = models.CharField(max_length=255)

    def member_names(self):
        return ', '.join(('{} {}'.format(m.first_name, m.last_name) for m in self.members.all()))

    def __str__(self):
        return self.name


@receiver(post_save, sender=TrackType)
def tracktype_verify_owner_is_member(sender, instance, created, *args, **kwargs):
    try:
        if created and instance.owner not in instance.members.all():
            instance.members.add(instance.owner)
    except:
        pass


class TrackRecord(models.Model):
    objects = TrackTypeManager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_tracks')
    type = models.ForeignKey(TrackType, on_delete=models.CASCADE, related_name='track_records')

    description = models.TextField(blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager(blank=True)

    def tag_list(self):
        return u", ".join(o.name for o in self.tags.all())

    def __str__(self):
        return '{} - {}'.format(self.user, self.type)


class QuickAction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quick_actions')
    type = models.ForeignKey(TrackType, on_delete=models.CASCADE, related_name='quick_actions')
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, default='blue')
    icon = models.CharField(max_length=255, blank=True, default='file_upload')
    description = models.TextField(blank=True, default='')
    tags = models.CharField(max_length=255, blank=True, default='', help_text='Comma separated tag names.')

    def __str__(self):
        return '{} {}'.format(self.user, self.type)
