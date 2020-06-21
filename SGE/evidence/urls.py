"""Evidence URL configuration"""

# Django
from django.urls import path

# Views
from evidence.views import ListEvidenceView, DetailEvideceView, CreateEvidenceView

urlpatterns = [
    path('create/', CreateEvidenceView.as_view()),
    path('list/<pk>/', ListEvidenceView.as_view()),
    path('detail/<pk>/', DetailEvideceView.as_view()),
]
