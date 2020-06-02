"""User URL configuration"""

# Django
from django.urls import path, include

# Views
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('<str:username>/', views.UserDetailView.as_view())
]
