from django import forms
from django.forms import DateTimeInput

from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    new_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'new_tags']
        widgets = {
            'deadline': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
