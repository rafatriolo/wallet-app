from django.test import SimpleTestCase
from django.urls import reverse, resolve
from walletapp.views import WalletDetailView

class WalletURLTest(SimpleTestCase):
    def test_wallet_detail_url(self):
        """Testa o mapeamento de URL para a view correta"""
        url = reverse("wallet-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, WalletDetailView)
