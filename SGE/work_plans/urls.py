"""Work plan URL configuration"""

# Django
from django.urls import path

# Views
from work_plans import views

urlpatterns = [
    path('create/', views.CreateWorkplanView.as_view()),
    path('list/<pk>/', views.ListWorkPlanView.as_view()),
    path('detail/<pk>/', views.DetailWorkPlanView.as_view()),
]