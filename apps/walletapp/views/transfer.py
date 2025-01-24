from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.walletapp.models import Transfer
from apps.walletapp.serializers import TransferSerializer


class CreateTransferView(APIView):
    """Criar uma transferência entre carteiras."""

    def post(self, request):
        serializer = TransferSerializer(data=request.data)
        
        if serializer.is_valid():
            # Salvar a transferência (chama o método create do serializer)
            transfer = serializer.save()

            # Retornar a resposta
            return Response(
                {
                    "message": "Transferência realizada com sucesso!",
                    "transfer": {
                        "id": transfer.id,
                        "sender": transfer.sender.user.username,
                        "receiver": transfer.receiver.user.username,
                        "amount": str(transfer.amount),
                        "timestamp": transfer.timestamp,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTransfersView(APIView):
    def get(self, request, user_id):
        # Obter parâmetros de data da query string
        start_date = request.query_params.get("start_date")  # Ex: 2023-01-01
        end_date = request.query_params.get("end_date")  # Ex: 2023-12-31

        try:
            # Filtrar transferências realizadas pelo usuário (remetente)
            transfers = Transfer.objects.filter(sender__user__id=user_id)

            # Aplicar filtro por período de data (se fornecido)
            if start_date:
                transfers = transfers.filter(
                    timestamp__gte=datetime.strptime(start_date, "%Y-%m-%d")
                )
            if end_date:
                transfers = transfers.filter(
                    timestamp__lte=datetime.strptime(end_date, "%Y-%m-%d")
                )

            # Serializar os dados
            serializer = TransferSerializer(transfers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
