from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from todoApp.todos.models import Todo
from todoApp.todos.serializers import TodoSerializer

class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        qs = Todo.objects.all()

        category = self.request.query_params.get('category')
        is_done = self.request.query_params.get('is_done')

        if category:
            qs = qs.filter(category__name=category)
        
        if is_done:
            qs = qs.filter(state=is_done.lower() == 'true')

        return qs