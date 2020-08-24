from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SnippetList(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permissions_classes = (IsAuthenticated,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'code_snippet')
    

# class SnippetDetail(viewsets.ModelViewSet):
#     """ Retrieve, update or delete a code snippet """
#     authentication_classes = (BasicAuthentication,)
#     permissions_classes = (IsAuthenticated,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

