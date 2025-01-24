from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Wallet


@receiver(post_save, sender=User)
def create_wallet_for_user(sender, instance, created, **kwargs):
    """Cria automaticamente uma carteira para cada usuário criado."""
    if created:
        Wallet.objects.create(user=instance)
