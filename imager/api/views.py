from rest_framework import viewsets, status
from imager.models import Snippets
from imager.api.serializers import SnippetsSerializer


class SnippetsViewSet(viewsets.ModelViewSet):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer

