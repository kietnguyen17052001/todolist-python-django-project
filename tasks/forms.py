from django import forms
from .models import Task
class TaskForm(forms.Form):
    name = forms.CharField(label='', required=True, 
                           widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter new task...'}),
                           max_length=255)
    # class Meta:
    #     model = Task
    #     fields = [
    #         'name',
    #         'category',
    #     ]
