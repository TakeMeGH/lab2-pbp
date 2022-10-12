from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views import View
import datetime
from django.shortcuts import redirect
from django.core import serializers

from todolist.forms import FormTodolist
from todolist.models import TodolistItem

@login_required(login_url='/todolist/login/')
def show_todolist(request):
  todolist_data = TodolistItem.objects.filter(user=request.user)
 
  form = FormTodolist()
  context = {
    'nama' : request.user.username,
    'todolist' : todolist_data,
    "form" : form,
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

@login_required(login_url='/todolist/login/')
def add(request):
    if request.method == 'POST':
        description = request.POST.get("description")
        title = request.POST.get("title")

        new_barang = TodolistItem(user=request.user, description=description, title=title)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def delete(request, id):
    todolist_data = TodolistItem.objects.filter(id=id)
    todolist_data.delete()
    return HttpResponseRedirect('/todolist')

@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist_item = TodolistItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))

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