from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'task_list'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('taskslist')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url =  reverse_lazy('taskslist')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =  reverse_lazy('taskslist')
