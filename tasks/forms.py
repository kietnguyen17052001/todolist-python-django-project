from django import forms
from .models import Task
class TaskForm(forms.Form):
    name = forms.CharField(label='Name', required=False, 
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           max_length=255)
    # class Meta:
    #     model = Task
    #     fields = [
    #         'name',
    #         'category',
    #     ]
