"""SGE URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('subject/', include('subjects.urls')),
    path('workplan/', include('work_plans.urls')),
]
