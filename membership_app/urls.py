from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/groups', views.groups),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/add_group', views.add_group),
    path('user/edit_group/<int:group_id>', views.edit_group),
    path('user/delete_group/<int:group_id>', views.delete_group)
]