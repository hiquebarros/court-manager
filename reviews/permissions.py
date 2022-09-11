from rest_framework import permissions
        
class ReviewCustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        
        if request.method == 'PATCH':
            return request.user.is_owner and request.user.id == obj.user_id

        if request.method == 'DELETE':
            return request.user.is_superuser or (request.user.is_owner and request.user.id == obj.user_id)
        
        return True
        