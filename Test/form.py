from .models import TodoList
from django.forms import ModelForm

class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        # fields = "__all__"
        fields = ['task']

