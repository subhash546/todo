from django.urls import path,include
from .views import add

urlpatterns = [
    path('add',add,name="addTask")
]

