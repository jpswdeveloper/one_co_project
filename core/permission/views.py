from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Permission
from .serializer import PermissionSerializer


# Create your views here.
class PermissionView(APIView):
    def get(self, request):
        permission = Permission.objects.all()
        instance = PermissionSerializer(permission, many=True)

        return Response(instance.data, status=status.HTTP_200_OK)

    def post(self, request):
        instance = PermissionSerializer(data=request.data)
        if instance.is_valid():
            instance.save()
            return Response(instance.data, status=status.HTTP_201_CREATED)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)
