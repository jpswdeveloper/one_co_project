from rest_framework import serializers
from .models import Permission, RolePermission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

    def create(self, validated_data):
        instance = Permission.objects.create(**validated_data)
        RolePermission.objects.all().delete()

        return instance

    def validate(self, data):
        if data["name"] is None:
            raise serializers.ValidationError("Role Name is required")
        return data
