from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import redirect

from todolist.forms import FormTodolist
from todolist.models import TodolistItem

@login_required(login_url='/todolist/login/')
def show_todolist(request):
  todolist_data = TodolistItem.objects.filter(user=request.user)
  context = {
    'nama' : request.user.username,
    'todolist' : todolist_data,
  }
  return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_more_task(request):
  if request.POST:
    form = FormTodolist(request.POST)
    if form.is_valid():
      task_list = form.save(commit=False)
      task_list.user = request.user
      task_list.save()
      form = FormTodolist()
      pesan = "Data berhasil disimpan"

      konteks = {
          "form" : form,
           "pesan" : pesan,
      }
      render(request, "create_task.html", konteks)
  else:
    form = FormTodolist()
    konteks = {
       "form" : form,
    }
  return render(request, "create_task.html", konteks)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def hapus_task(request, id_task):
  todolist_data = TodolistItem.objects.filter(id=id_task)
  todolist_data.delete()
  return redirect('todolist:show_todolist')

def ganti_status(request, id_task):
  todolist_data = TodolistItem.objects.get(id=id_task)
  todolist_data.is_finished = bool(1 - int(todolist_data.is_finished))
  todolist_data.save()
  return redirect('todolist:show_todolist')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response