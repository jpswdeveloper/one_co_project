from rest_framework import serializers
from .models import Role
from permission.serializer import PermissionSerializer
from permission.models import Permission, RolePermission


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(), many=True
    )
    business_owner_id = serializers.UUIDField(required=False)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions_data = validated_data.pop("permissions")
        business_owner_id = validated_data.pop("business_owner_id", None)
        role = Role.objects.create(**validated_data)
        role.permissions.set(permissions_data)

        # Create RolePermission instances with the provided business_owner_id
        for permission in permissions_data:
            role_permission = RolePermission(
                role=role, permission=permission, business_owner_id=business_owner_id
            )
            role_permission.save()

        return role
