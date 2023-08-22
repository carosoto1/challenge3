from django.shortcuts import render
from rest_framework import generics
from account.models import Account
from .serializers import AccountSerializer


# Create your views here.
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer