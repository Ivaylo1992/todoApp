from django.urls import path
from todoApp.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]