from rest_framework import viewsets
from livros.api import serializers
from livros import models

class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()