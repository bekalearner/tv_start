from rest_framework import permissions


class Editor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editor').exists()