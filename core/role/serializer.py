from rest_framework import serializers
from .models import Role
from permission.models import Permission, RolePermission
from permission.serializer import PermissionSerializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RolePermissonSerializer(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),  # Query all Permission objects
        required=True,
        write_only=True,
    )
    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),  # Query all Permission objects
        required=True,
        write_only=True,
    )
    business_owner_id = serializers.UUIDField(
        required=False, write_only=False, allow_null=True
    )

    class Meta:
        model = RolePermission
        fields = [
            "permission",
            "role",
            "business_owner_id",
        ]

    def validate(self, attrs):
        permission = attrs.get("permission")
        if not permission:
            raise serializers.ValidationError("Permissions are required.")

        # No need to check if permission exists since PrimaryKeyRelatedField ensures validity
        return attrs

    def create(self, validated_data):
        return RolePermission.objects.create(**validated_data)
