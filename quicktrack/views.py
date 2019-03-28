import collections

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from .models import TrackType, TrackRecord, QuickAction
from .tables import TrackingTable

from .filters import TrackingFilter
from .forms import DeleteForm, TrackRecordForm, TrackTypeForm, QuickActionForm


@login_required
def index(request):
    context = {'title': 'Home|Quick Track'}
    params = {k: v for k, v in request.GET.items() if v != ''}

    f = TrackingFilter(params, queryset=TrackRecord.objects.with_user(request.user), request=request)
    table = TrackingTable(f.qs)

    context['actions'] = [act for act in QuickAction.objects.filter(user=request.user)]
    context['filter'] = f
    context['table'] = table

    return render(request, 'quicktrack/index.html', context)


@login_required
def track_record_update(request, pk=None):
    context = {'title': 'Update Record|Quick Track'}

    try:
        record = TrackRecord.objects.get(pk=pk)
    except (TrackRecord.DoesNotExist, Exception):
        record = None

    if request.method == 'POST':
        form = TrackRecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            return redirect('quicktrack:home')
    else:
        form = TrackRecordForm(initial={'user': request.user})

    context['form'] = form
    context['record'] = record

    return render(request, 'quicktrack/track_record_update.html', context)


@login_required
def track_record_delete(request, pk):
    context = {'title': 'Delete Record|Quick Track'}

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            try:
                TrackRecord.objects.get(pk=form.cleaned_data['pk']).delete()
            except (TrackRecord.DoesNotExist, Exception):
                msg = 'Could not delete the track record!\nOther objects are using this track record.'
                messages.error(request, msg)
            return redirect('quicktrack:home')
    else:
        form = DeleteForm(initial={'pk': pk})

    context['form'] = form
    return render(request, 'quicktrack/delete_form.html', context)


@login_required
def actions_quick_add(request, pk):
    act = get_object_or_404(QuickAction, pk=pk)
    if act.type not in TrackType.objects.with_user(request.user):
        raise PermissionDenied

    tr = TrackRecord.objects.create(user=request.user, type=act.type, description=act.description)
    if act.tags:
        tr.tags.add(*(a.strip() for a in act.tags.split(',')))
    return redirect('quicktrack:home')


# ========== Track Type ==========
@login_required
def track_type_list(request):
    context = {'title': 'List Type|Quick Track'}

    track_types = TrackType.objects.with_user(request.user)

    context['track_types'] = track_types

    return render(request, 'quicktrack/track_type_list.html', context)


@login_required
def track_type_update(request, pk=None):
    context = {'title': 'Update Type|Quick Track'}

    try:
        track_type = TrackType.objects.get(pk=pk)
    except (TrackType.DoesNotExist, Exception):
        track_type = None

    if request.method == 'POST':
        form = TrackTypeForm(request.POST, instance=track_type)
        if form.is_valid():
            form.save()
            return redirect('quicktrack:home')
    else:
        form = TrackTypeForm(initial={'owner': request.user}, instance=track_type)

    context['form'] = form
    context['track_type'] = track_type

    return render(request, 'quicktrack/track_type_update.html', context)


@login_required
def track_type_delete(request, pk):
    context = {'title': 'Delete Type|Quick Track'}

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            try:
                TrackType.objects.get(pk=form.cleaned_data['pk']).delete()
            except (TrackType.DoesNotExist, Exception):
                messages.error(request, 'Could not delete the track type!\nOther objects are using this track type.')
            return redirect('quicktrack:home')
    else:
        form = DeleteForm(initial={'pk': pk})

    context['form'] = form
    return render(request, 'quicktrack/delete_form.html', context)


# ========== Quick Actions ==========
@login_required
def actions_list(request):
    context = {'title': 'List Actions|Quick Track'}

    actions = QuickAction.objects.filter(user=request.user)

    context['actions'] = actions

    return render(request, 'quicktrack/actions_list.html', context)


@login_required
def actions_update(request, pk=None):
    context = {'title': 'Update Action|Quick Track'}

    try:
        action = QuickAction.objects.get(pk=pk)
    except (TrackType.DoesNotExist, Exception):
        action = None

    if request.method == 'POST':
        form = QuickActionForm(request.POST, instance=action)
        if form.is_valid():
            form.save()
            return redirect('quicktrack:home')
    else:
        form = QuickActionForm(initial={'user': request.user}, instance=action)

    context['form'] = form
    context['action'] = action

    return render(request, 'quicktrack/actions_update.html', context)


@login_required
def actions_delete(request, pk):
    context = {'title': 'Delete Action|Quick Track'}

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            try:
                QuickAction.objects.get(pk=form.cleaned_data['pk']).delete()
            except (QuickAction.DoesNotExist, Exception):
                msg = 'Could not delete the quick action!\nOther objects are using this quick action.'
                messages.error(request, msg)
            return redirect('quicktrack:home')
    else:
        form = DeleteForm(initial={'pk': pk})

    context['form'] = form
    return render(request, 'quicktrack/delete_form.html', context)
