from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.walletapp.models import User, Wallet
from apps.walletapp.serializers import AddBalanceSerializer, WalletSerializer


class WalletDetailView(APIView):
    """Consultar saldo de uma carteira."""

    def get(self, request, user_id):
        try:
            wallet = Wallet.objects.get(user__id=user_id)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data)
        except Wallet.DoesNotExist:
            return Response(
                {"error": "Carteira não encontrada"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CreateWalletView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            if hasattr(
                user, "wallet"
            ):  # Verifica se o usuário já tem uma carteira
                return Response(
                    {"error": "Usuário já possui uma carteira."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Cria a carteira
            wallet = Wallet.objects.create(user=user)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuário não encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )


class AddBalanceView(APIView):
    """Endpoint para adicionar saldo à carteira de um usuário."""

    def post(self, request, user_id):
        try:
            wallet = Wallet.objects.get(user__id=user_id)
        except Wallet.DoesNotExist:
            return Response(
                {"error": "Carteira não encontrada para o usuário."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AddBalanceSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data["amount"]
            wallet.add_balance(amount)  # Adiciona saldo
            return Response(
                {
                    "message": "Saldo adicionado com sucesso!",
                    "balance": str(wallet.balance),
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
