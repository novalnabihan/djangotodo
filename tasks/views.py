from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('taskslist')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('taskslist')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url =  reverse_lazy('taskslist')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =  reverse_lazy('taskslist')
