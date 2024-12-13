from django.urls import path, re_path  # Use path or re_path
from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView,
    CreateAccountAPIView,
    AccountListAPIView
)

urlpatterns = [
    path('branches/', BranchesAPIView.as_view(), name='branches'),
    re_path(r'^branch/(?P<pk>[0-9]+)/$', BranchDetailAPIView.as_view(), name='branch-detail'),
    path('banks/', BanksAPIView.as_view(), name='banks'),
    re_path(r'^bank/(?P<pk>[0-9]+)/$', BankDetailAPIView.as_view(), name='bank-detail'),
    path('create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    path('accounts/', AccountListAPIView.as_view(), name='accounts'),
]
