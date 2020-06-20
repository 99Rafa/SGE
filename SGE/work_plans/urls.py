"""Work plan URL configuration"""

# Django
from django.urls import path

# Views
from work_plans import views

urlpatterns = [
    path('list/<pk>/', views.ListWorkPlanView.as_view()),
    path('detail/<pk>/', views.DetailWorkPlanView.as_view()),
]