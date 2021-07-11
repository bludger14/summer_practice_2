from .models import Task, Song
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Исполнитель'
            }),

        }


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ["title", "artist", "image", "audio_file", "audio_link", "duration"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "artist": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "image": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
        }