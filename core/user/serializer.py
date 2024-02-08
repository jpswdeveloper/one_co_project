from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User

from role.models import Role


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    roleId = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),  # Query all Permission objects
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ("id", "email", "is_active", "is_staff", "password", "roleId", "phone")

    # def validate_email(self, value):
    def validate_email(self, value):
        # check if there is an exisiting email
        email_checker = User.objects.filter(email=value)
        if email_checker:
            raise ValidationError("Email already exists")
        return value

    def validate_phone(self, value):
        # check if there is an exisiting email
        phone_checker = User.objects.filter(phone=value)
        if phone_checker:
            raise ValidationError("Phone already exists")
        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise ValidationError(e.messages)
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.roleId = validated_data.get("roleId", instance.roleId)
        instance.profile_image = validated_data.get("profile_pic", instance.profile_pic)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_staff = validated_data.get("is_staff", instance.is_staff)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.set_password(validated_data.get("password", instance.password))
        instance.save()
        return instance
