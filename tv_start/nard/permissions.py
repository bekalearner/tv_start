from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import permissions

from .models import Backgammon


# Получаем тип модели для объектов Match
content_type = ContentType.objects.get_for_model(Backgammon)

# Получаем разрешения для модели Match
add_backgammon_permission = Permission.objects.get(
    codename='add_backgammon', content_type=content_type)
change_backgammon_permission = Permission.objects.get(
    codename='change_backgammon', content_type=content_type)
delete_backgammon_permission = Permission.objects.get(
    codename='delete_backgammon', content_type=content_type)
view_backgammon_permission = Permission.objects.get(
    codename='view_backgammon', content_type=content_type)

# Создаем группу редакторов, если она еще не существует
editors, created = Group.objects.get_or_create(name='Editors')

# Добавляем разрешения для группы редакторов
if created:
    editors.permissions.add(
        add_backgammon_permission, change_backgammon_permission,
        delete_backgammon_permission, view_backgammon_permission)

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editors').exists()