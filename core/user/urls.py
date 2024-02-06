from django.urls import path
from .views import User_View

urlpatterns = [
    path("user/<int:userId>", User_View.as_view()),
    path("user/", User_View.as_view()),
]
