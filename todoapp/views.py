from datetime import date

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from todoapp.models import Task


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tasks = Task.objects.all().count()
    num_due_today = Task.objects.filter(due_date__exact=date.today()).count()
    num_overdue = Task.objects.filter(due_date__lt=date.today()).count()
    num_high_priority = Task.objects.filter(priority='h').count()

    context = {
        'num_tasks': num_tasks,
        'num_due_today': num_due_today,
        'num_overdue': num_overdue,
        'num_high_priority': num_high_priority,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
