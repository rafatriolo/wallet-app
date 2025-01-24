from django.apps import AppConfig


class WalletappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.walletapp"

    def ready(self):
        import apps.walletapp.signals as signals

        _ = signals
