from django.urls import path
from .views import PermissionView


urlpatterns = [
    path("permission/", PermissionView.as_view(), name="Permission"),
]
