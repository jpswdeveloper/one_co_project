from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RolePermissonSerializer, RoleSerializer
from .models import Role
from permission.models import Permission


class RoleAPIView(APIView):

    def get(self, request, *args, **kwargs):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        role_serializer = RoleSerializer(data=request.data)
        if role_serializer.is_valid():
            role = role_serializer.save()

            permissions_list = request.data.get("permissions", [])
            business_owner_id = request.data.get("business_owner_id", None)

            for perm_id in permissions_list:
                try:
                    permission = Permission.objects.get(id=perm_id)
                except Permission.DoesNotExist:
                    return Response(
                        {"error": f"Permission with UUID {perm_id} does not exist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                role_permission_data = {
                    "role": role.id,
                    "permission": permission.id,  # Assign the Permission instance
                    "business_owner_id": business_owner_id,
                }

                role_permission_serializer = RolePermissonSerializer(
                    data=role_permission_data
                )

                if role_permission_serializer.is_valid():
                    role_permission_serializer.save()
                else:
                    return Response(
                        role_permission_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response(
                {"message": "Role created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
