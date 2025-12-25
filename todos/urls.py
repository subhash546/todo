from django.urls import path,include
from .views import add,completedTask,uncompletedTask,deletetask,edit

urlpatterns = [
    path('add',add,name="addTask"),
    path("markdone/<int:pk>",completedTask,name="taskcompleted"),
    path("markundone/<int:pk>",uncompletedTask,name="tasknotdone"),
    path("delete/<int:pk>",deletetask,name="delete"),
    path("edittask/<int:pk>",edit,name="edit")
]

