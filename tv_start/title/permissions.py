from title.models import Article
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import permissions
# Получаем тип модели для объектов Article
content_type = ContentType.objects.get_for_model(Article)

# Получаем разрешения для модели Article
add_article_permission = Permission.objects.get(
    codename='add_article', content_type=content_type)
change_article_permission = Permission.objects.get(
    codename='change_article', content_type=content_type)
delete_article_permission = Permission.objects.get(
    codename='delete_article', content_type=content_type)
view_article_permission = Permission.objects.get(
    codename='view_article', content_type=content_type)

# Создаем группу редакторов, если она еще не существует
editors, created = Group.objects.get_or_create(name='Editors')

# Добавляем разрешения для группы редакторов
if created:
    editors.permissions.add(
        add_article_permission, change_article_permission,
        delete_article_permission, view_article_permission)



class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editors').exists()
