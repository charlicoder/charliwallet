
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('', include('charliauth.urls')),
    path('dashboard/', TemplateView.as_view(template_name="dashboard/index.html"), name="dashboard"),
    path('poll/', include('poll.urls')),
    path('employee/', include('employee.urls')),
    path('admin/', admin.site.urls),
]
