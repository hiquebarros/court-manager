from rest_framework import permissions
from facilities.models import Facility

import ipdb


class IsFacilityOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        facility_id = view.kwargs["facility_id"]
        facility_owner = Facility.objects.get(id=facility_id)

        return request.user == facility_owner.user


class IsFacilityOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        facility_owner = Facility.objects.get(id=obj.sport_facility.id)

        return (request.user == facility_owner.user) or request.user.is_superuser