from django.db import models

from .user import User


class Wallet(models.Model):
    """Modelo que representa a carteira do usuário."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="wallet"
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def add_balance(self, amount):
        """Adiciona saldo à carteira."""
        self.balance += amount
        self.save()

    def subtract_balance(self, amount):
        """Subtrai saldo da carteira."""
        if amount > self.balance:
            raise ValueError("Saldo insuficiente!")
        self.balance -= amount
        self.save()

    def __str__(self):
        return f"Carteira de {self.user.username} - Saldo: {self.balance}"

    def get_transfers(self, start_date=None, end_date=None):
        """Lista as transferências realizadas com filtro opcional por data."""
        transfers = self.sent_transfers.all()
        if start_date:
            transfers = transfers.filter(timestamp__gte=start_date)
        if end_date:
            transfers = transfers.filter(timestamp__lte=end_date)
        return transfers
