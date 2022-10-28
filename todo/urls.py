from django.urls import path

from todo.views import todo_list_view, create_users

urlpatterns = [
    path("list/",todo_list_view, name= 'index'),
    path("createusers/",create_users, name = "createusers")
]