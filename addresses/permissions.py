from rest_framework import permissions
from rest_framework.views import Request, View

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view:View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_owner

    
class IsFacilityOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, facility):
        return request.user.id == facility.user.id:
            
