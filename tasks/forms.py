from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from functools import partial
from bootstrap_datepicker_plus import DateTimePickerInput

# DateInput = partial(forms.DateTimeInput, {'class': 'datepicker'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'duedate': DateTimePickerInput(),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2']