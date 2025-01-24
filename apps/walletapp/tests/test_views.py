from django.test import TestCase
from rest_framework.test import APIClient
from walletapp.models import Wallet, User

class WalletDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.wallet = Wallet.objects.create(user=self.user, balance=100.0)
        self.client = APIClient()

    def test_get_wallet_detail(self):
        """Testa o endpoint de detalhe da carteira"""
        response = self.client.get(f"/wallet/{self.user.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["balance"], 100.0)
