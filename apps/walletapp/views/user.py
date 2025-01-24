from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.walletapp.serializers import UserSerializer


class CreateUserView(APIView):
    """Endpoint para criar um novo usuário."""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Usuário criado com sucesso!",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
