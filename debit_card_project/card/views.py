from django.shortcuts import render
from rest_framework import generics
from card.models import Card
from .serializers import CardSerializer


# Create your views here.
class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer