from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length = 200, blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    compile = models.BooleanField(default = False)
    date = models.DateField(auto_now_add = True, editable = False)