from django.urls import path
from todoApp.todos import views

urlpatterns = [
    path('', views.TodoListCreateAPIView.as_view(), name='todos_list_create')
]