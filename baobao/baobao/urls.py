"""
Definition of urls for baobao.
"""

from datetime import datetime
from xml.etree.ElementInclude import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test', views.test),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('admin', admin.site.urls),
    path('accounts/logout/', views.log_out, name='logout'),
    path('register', views.sign_up, name='Register'),
    path('accounts/login/', views.sign_in, name='login'),
    path('accounts/profile/', views.home),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),      
    path("password_reset", views.password_reset_request, name="password_reset")
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
