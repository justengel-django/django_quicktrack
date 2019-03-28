from django.urls import path, include
from quicktrack import views


app_name = 'quicktrack'


urlpatterns = [
    path('', views.index, name='home'),

    path('record/new', views.track_record_update, name='record_new'),
    path('record/delete/<int:pk>', views.track_record_delete, name='record_delete'),
    path('record/quick/<int:pk>', views.actions_quick_add, name='record_quick'),

    path('type/list', views.track_type_list, name='type_list'),
    path('type/new', views.track_type_update, name='type_new'),
    path('type/edit/<int:pk>', views.track_type_update, name='type_edit'),
    path('type/delete/<int:pk>', views.track_type_delete, name='type_delete'),

    path('actions/list', views.actions_list, name='actions_list'),
    path('actions/new', views.actions_update, name='actions_new'),
    path('actions/edit/<int:pk>', views.actions_update, name='actions_edit'),
    path('actions/delete/<int:pk>', views.actions_delete, name='actions_delete'),
]
