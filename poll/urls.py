from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

app_name = 'poll'
urlpatterns = [
    path('', index, name='polls_home'),
    path('add/', poll_add, name='poll_add'),
    path('<int:id>/details/', details, name='poll_details'),
    path('<int:id>/', update_poll, name='update_poll'),
]
