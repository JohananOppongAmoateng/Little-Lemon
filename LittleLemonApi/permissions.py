from rest_framework.permissions import BasePermission

class IsManagerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.groups.filter(name='Manager').exists():
            return True
        
        return False

class IsManager(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Manager').exists():
            return True
        
        return False