from django.urls import path
from todoApp.accounts import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token')
]