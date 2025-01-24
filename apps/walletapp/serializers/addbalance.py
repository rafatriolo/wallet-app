from rest_framework import serializers


class AddBalanceSerializer(serializers.Serializer):
    """Serializer para adicionar saldo."""

    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_amount(self, value):
        """Verifica se o valor é positivo."""
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser positivo.")
        return value
