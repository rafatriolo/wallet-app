from django.test import TestCase
from walletapp.models import Wallet, User

class WalletModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.wallet = Wallet.objects.create(user=self.user, balance=100.0)

    def test_wallet_creation(self):
        """Testa se a carteira é criada corretamente"""
        self.assertEqual(self.wallet.user.username, "testuser")
        self.assertEqual(self.wallet.balance, 100.0)

    def test_add_balance(self):
        """Testa o método add_balance"""
        self.wallet.add_balance(50.0)
        self.assertEqual(self.wallet.balance, 150.0)

    def test_subtract_balance(self):
        """Testa o método subtract_balance"""
        self.wallet.subtract_balance(20.0)
        self.assertEqual(self.wallet.balance, 80.0)
