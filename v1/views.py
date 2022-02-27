from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
import requests
from .models import ScoreCard
from .serializer import ScoreCardSerializer



# Create your views here.
class CardList(generics.ListAPIView):
    queryset = ScoreCard.objects.all()
    serializer_class = ScoreCardSerializer
    #filter_backends = [DjangoFilterBackend]
    filter_fields = ('Hand', 'Card_Type', 'Card_Value_Type', 'Tricks', 'Vulnerable', 'Trick_Points')
