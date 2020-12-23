from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', index, name='polls_home'),
    path('<int:id>/details/', details, name='poll_details'),
    path('<int:id>/', update_poll, name='update_poll'),
]
