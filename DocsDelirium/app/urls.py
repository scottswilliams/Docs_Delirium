# posts/urls.py
from django.urls import path

from .views import index, cartoon_detail

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', cartoon_detail, name='cartoon-detail')
]