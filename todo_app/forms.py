from .models import Todo
from django import forms


class TodoForm(forms.Form):
    name = forms.CharField(label='', max_length=100,
             widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'Add Todo'}))
