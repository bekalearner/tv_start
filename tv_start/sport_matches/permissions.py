from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import permissions

from sport_matches.models import Match


# Получаем тип модели для объектов Match
content_type = ContentType.objects.get_for_model(Match)

# Получаем разрешения для модели Match
add_match_permission = Permission.objects.get(
    codename='add_match', content_type=content_type)
change_match_permission = Permission.objects.get(
    codename='change_match', content_type=content_type)
delete_match_permission = Permission.objects.get(
    codename='delete_match', content_type=content_type)
view_match_permission = Permission.objects.get(
    codename='view_match', content_type=content_type)

# Создаем группу редакторов, если она еще не существует
editors, created = Group.objects.get_or_create(name='Editors')

# Добавляем разрешения для группы редакторов
if created:
    editors.permissions.add(
        add_match_permission, change_match_permission,
        delete_match_permission, view_match_permission)

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editors').exists()
