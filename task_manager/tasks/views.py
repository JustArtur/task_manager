from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserCreationForm, TaskCreationForm
from .models import *


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class TaskView(LoginRequiredMixin, View):
    template_name = 'index.html'
    login_url = 'login'

    def get(self, request):
        form = TaskCreationForm()
        tasks = Task.objects.filter(user_id=request.user.id).filter(completed=False).order_by('-created_at')
        completed_tasks = Task.objects.filter(user_id=request.user.id).filter(completed=True).order_by('-created_at')
        context = {
            'tasks': tasks,
            'completed_tasks': completed_tasks,
            'title': 'Главная страница',
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            try:
                portfolio = form.save(commit=False)
                portfolio.user_id = request.user.id
                form.save()
                return redirect('index')
            except:
                form.add_error(None, 'Произошла ошибка, повторите позже')
        else:
            return render(request, self.template_name, {'form': form})

    # def update(self, request, task_id):
    #     task = Task.objects.get(id=task_id)
    #     task.is_complete = not task.is_complete
    #     task.save()
    #     return redirect('index')
    #
    # def delete(self, request, task_id):
    #     task = Task.objects.get(id=task_id)
    #     task.delete()
    #     return redirect('index')


class TaskUpdateView(LoginRequiredMixin, View):
    template_name = 'index.html'
    login_url = 'login'

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('index')


class TaskDeleteView(LoginRequiredMixin, View):
    template_name = 'index.html'
    login_url = 'login'

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('index')
