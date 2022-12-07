from django.http import HttpResponse

from rest_framework import viewsets

from needs.models import Needs
from needs.serializer import NeedsSerializer

def hello(request):
    return HttpResponse("Hello, world! Ringo")

class NeedsViewSet(viewsets.ModelViewSet):
    queryset = Needs.objects.all()
    serializer_class = NeedsSerializer

