"""Subject URL configuration"""

# Django
from django.urls import path

# Views
from subjects import views

urlpatterns = [
    path('get_subjects/', views.get_subjects_view),
]