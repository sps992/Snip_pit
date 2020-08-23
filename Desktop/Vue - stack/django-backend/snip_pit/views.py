from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter


class SnippetList(generics.ListCreateAPIView):
    """ List all snippets, or create a new snippet """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'code_snippet')
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a code snippet """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer