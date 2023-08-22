from django.urls import path
from account.views import AccountList, AccountDetail

urlpatterns = [
    path('account/', AccountList.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
]