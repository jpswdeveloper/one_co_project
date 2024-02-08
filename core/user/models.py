from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from role.models import Role

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field must be set")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE, null=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
