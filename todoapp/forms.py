from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
    due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)

    class Meta:
        model = Task
        fields =[
            'title' , 'due'
        ]
	
class UpdateForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)

    class Meta:
        model= Task
        fields =[
            'title', 'due' , 'completd'
        ]




  ##  "workbench.colorTheme": "One Dark Pro",
    ##"files.autoSave": "afterDelay",