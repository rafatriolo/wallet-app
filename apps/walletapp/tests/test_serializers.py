from django.test import TestCase
from walletapp.models import Wallet, User
from walletapp.serializers import WalletSerializer

class WalletSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.wallet = Wallet.objects.create(user=self.user, balance=100.0)
        self.serializer = WalletSerializer(instance=self.wallet)

    def test_serializer_data(self):
        """Testa os dados serializados"""
        data = self.serializer.data
        self.assertEqual(data["user"], self.user.id)
        self.assertEqual(data["balance"], "100.00")
