"""
Definition of urls for DocsDelirium.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('app.urls')),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('.well-known/pki-validation/D14F33A65B9A2A8F41CDFCCEDC118917.txt/', TemplateView.as_view(template_name="D14F33A65B9A2A8F41CDFCCEDC118917.txt", content_type="text/plain"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)