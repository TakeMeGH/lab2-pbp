from django.forms import ModelForm
from django import forms
from todolist.models import TodolistItem

class FormTodolist(ModelForm):
    class Meta:
        model = TodolistItem
        fields = ['title', 'description']

        widgets = {
            'title' : forms.TextInput({'class':'form-control'}),   
            'description' : forms.Textarea({'class':'form-control'}),    
        }