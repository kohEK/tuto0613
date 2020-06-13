from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # PUT, DELETE 요청에 한해, 작성자에게만 허용****
        return obj.author == request.user
