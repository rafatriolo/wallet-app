from rest_framework import serializers
from .user import UserSerializer
from apps.walletapp.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Inclui os detalhes do usuário

    class Meta:
        model = Wallet
        fields = ["id", "user", "balance"]
        read_only_fields = ["id", "balance"]
