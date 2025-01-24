from django.db import models
from .wallet import Wallet


class Transfer(models.Model):
    """Modelo que representa as transferências entre carteiras."""

    sender = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="sent_transfers"
    )
    receiver = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="received_transfers"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Transferência de {self.sender.user.username} para "
            f"{self.receiver.user.username} - R$ {self.amount}"
        )
