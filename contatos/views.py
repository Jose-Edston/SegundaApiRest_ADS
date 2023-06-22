from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from contatos.models import Contatos
from contatos.serializers import ContatosSerializer


class ContatosViewSet(viewsets.ModelViewSet):
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer

