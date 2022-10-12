from django.contrib import admin
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
  path('', show_todolist, name='show_todolist'),
  path('register/', register, name='register'),
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),
  path('create-task/', create_more_task, name='create_more_task'),
  path('hapus-task/<int:id_task>', hapus_task, name="hapus_task"),
  path('ganti-status/<int:id_task>', ganti_status, name="ganti_status"),
  path('json/', get_todolist_json, name="get_todolist_json"),
  path('add/', add, name="add"),
  path('delete/<int:id>', delete, name="delete"),


]