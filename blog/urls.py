from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),
    # path('<int:id>/', update_poll, name='update_poll'),
]
