from django.urls import path
from .views import RoleAPIView

urlpatterns = [
    path("role/", RoleAPIView.as_view(), name="Role"),
]
