from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Responsible for crud user functionality


class User_View(APIView):
    def get(self, request, userId=None):
        if userId:
            # If userId is provided, retrieve a specific user
            try:
                user = User.objects.get(id=userId)
            except User.DoesNotExist:
                return Response(
                    {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            # If no user_id is provided, retrieve a list of all users
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Assuming data is available in request.data
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # Save the user
            serializer.save()

            # You might want to customize the response based on your needs
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, userId):
        try:
            user = User.objects.get(pk=userId)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userId):
        try:
            user = User.objects.get(pk=userId)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response({"message": "Ok"})
