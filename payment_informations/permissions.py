from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

from .models import PaymentInformation

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        
        return request.user == obj.user
    
class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        
        return request.user.is_authenticated

