from django.urls import path
from snip_pit import views
from rest_framework import routers
# urlpatterns = [
#     path('snip-pit/', views.SnippetList.as_view()),
#     path('snip-pit/<int:pk>/', views.SnippetDetail.as_view()),
# ]

router = routers.DefaultRouter()
router.register(r'', views.SnippetList)

urlpatterns = router.urls