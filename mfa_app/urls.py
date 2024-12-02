from django.urls import path
from . import views

urlpatterns = [
    path('enable-mfa/', views.enable_mfa, name='enable_mfa'),
    path('verify-mfa/', views.verify_mfa, name='verify_mfa'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
