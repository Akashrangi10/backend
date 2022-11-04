from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
import json

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


def todo_list_view(request):
    todo_data = Todo.objects.values('title','description','completed')
        
    # todo_datas = json.loads(todo_data[0])

    return render(request, 'todo/index.html',{'datas': todo_data})

def create_users(request):
    print("**************")
    return
