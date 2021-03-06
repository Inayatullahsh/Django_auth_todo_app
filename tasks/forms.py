from django import forms
from django.db import transaction

from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'form-control text-bloack-50',
                    'placeholder': '✍️ Add item...',
                    'autocomplete': 'off',
                    'autofocus': 'autofocus',
                    'aria-label': '✍️ Add item...',
                    'aria-describedby': 'button-addon2'
                }
            )
        }
