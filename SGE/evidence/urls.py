"""Evidence URL configuration"""

# Django
from django.urls import path

# Views
from evidence.views import EvidenceView, DetailEvideceView

urlpatterns = [
    path('list_create/', EvidenceView.as_view()),
    path('detail/<pk>/', DetailEvideceView.as_view()),
]
