from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework import viewsets 
from .serializers import MovieSerializer
from .models import MovieData 
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer 
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer
    
class DramaViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='drama')
    serializer_class = MovieSerializer 