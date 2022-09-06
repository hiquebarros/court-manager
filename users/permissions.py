from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method != "DELETE":
            return False
        
        return request.user.is_superuser and request.user.is_authenticated
        
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj and request.user.is_authenticated
        