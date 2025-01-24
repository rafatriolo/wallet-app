from rest_framework import serializers

from apps.walletapp.models import Transfer, Wallet



class TransferSerializer(serializers.ModelSerializer):
    sender_user_id = serializers.IntegerField(write_only=True)
    receiver_user_id = serializers.IntegerField(write_only=True)
    sender = serializers.SerializerMethodField()  # Apenas leitura
    receiver = serializers.SerializerMethodField()  # Apenas leitura

    class Meta:
        model = Transfer
        fields = [
            "id",
            "amount",
            "timestamp",
            "sender_user_id",
            "receiver_user_id",
            "sender",
            "receiver",
        ]
        read_only_fields = ["id", "timestamp", "sender", "receiver"]

    def validate(self, data):
        """Valida os dados antes de criar a transferência."""
        sender_user_id = data.get("sender_user_id")
        receiver_user_id = data.get("receiver_user_id")
        amount = data.get("amount")

        if sender_user_id == receiver_user_id:
            raise serializers.ValidationError(
                "O remetente e o destinatário não podem ser iguais."
            )

        try:
            sender_wallet = Wallet.objects.get(user__id=sender_user_id)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError(
                {"sender_user_id": "Carteira do remetente não encontrada."}
            )

        try:
            receiver_wallet = Wallet.objects.get(user__id=receiver_user_id)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError(
                {"receiver_user_id": "Carteira do destinatário não encontrada."}
            )

        if amount <= 0:
            raise serializers.ValidationError(
                {"amount": "O valor da transferência deve ser positivo."}
            )
        if sender_wallet.balance < amount:
            raise serializers.ValidationError(
                {"amount": "Saldo insuficiente na carteira do remetente."}
            )

        # Adiciona as carteiras validadas ao contexto
        self.context["sender_wallet"] = sender_wallet
        self.context["receiver_wallet"] = receiver_wallet
        return data

    def create(self, validated_data):
        """Cria a transferência após os dados serem validados."""
        sender_wallet = self.context["sender_wallet"]
        receiver_wallet = self.context["receiver_wallet"]
        amount = validated_data["amount"]

        # Atualizar saldos das carteiras
        sender_wallet.subtract_balance(amount)
        receiver_wallet.add_balance(amount)

        # Criar a transferência
        transfer = Transfer.objects.create(
            sender=sender_wallet,
            receiver=receiver_wallet,
            amount=amount,
        )
        return transfer

    def get_sender(self, obj):
        """Retorna detalhes do remetente."""
        user = obj.sender.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

    def get_receiver(self, obj):
        user = obj.receiver.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
