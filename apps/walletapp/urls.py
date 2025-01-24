from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Login para obter o token
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Atualizar token de acesso
    path(
        "wallet/<int:user_id>/",
        views.WalletDetailView.as_view(),
        name="wallet-detail",
    ),
    path("create-user/", views.CreateUserView.as_view(), name="create-user"),
    path(
        "create-wallet/",
        views.CreateWalletView.as_view(),
        name="create-wallet",
    ),
    path(
        "wallet/<int:user_id>/add-balance/",
        views.AddBalanceView.as_view(),
        name="add-balance",
    ),
    path(
        "transfer/", views.CreateTransferView.as_view(), name="create-transfer"
    ),
    path(
        "user/<int:user_id>/transfers/",
        views.UserTransfersView.as_view(),
        name="user-transfers",
    ),
]
