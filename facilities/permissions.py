import ipdb
from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

from facilities.models import Facility


class IsAOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view:View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_owner


class IsAOwnOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view:View) -> bool:
        return request.user.is_authenticated and request.user.is_owner

    def has_object_permission(self, request: Request, view: View, user: User):
        ipdb.set_trace()
        return request.user.id == user.id
