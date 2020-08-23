from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('created_by', 'title', 'description', 'code_snippet', 'linenos', 'language', 'style')