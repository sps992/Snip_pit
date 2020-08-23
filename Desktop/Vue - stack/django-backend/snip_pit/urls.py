from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snip_pit import views

urlpatterns = [
    path('snip-pit/', views.SnippetList.as_view()),
    path('snip-pit/<int:pk>/', views.SnippetDetail.as_view()),
]