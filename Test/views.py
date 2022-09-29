from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .form import TodoListForm
from .models import TodoList

# Create your views here.


# def index(request):
class Index(View):
    """Class Based Home view"""
    template = "Test/index.html"
    context = {}
    def get(self, request):
        self.context |=({
            "form": UserCreationForm()
        })
        return render(request, self.template, self.context)
    def post(self, request):
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(username)
        if pass1 == pass2:
            try:
                user = User.objects.create(username=username, password=pass1)
                login(request, user)
                return redirect('Home')
            except IndentationError:
                self.context |= ({
                    'message': "User Already Used"
                })
        else:
            self.context |= ({
                'message': "Password Not Match"
            })
        return render(request, self.template, self.context)


# def home(request):
#     pass 

class Home(View):
    """Crate list function"""
    template = "Test/home.html"
    context = {}
    def get(self, request):
        self.context |= ({
            'form': TodoListForm
        })
        return render(request, self.template, self.context)
    def post(self, request):
        task = request.POST.get('task')
        todoList = TodoList()
        todoList.user = request.user
        todoList.task = task 
        todoList.save()
        return redirect("Success")
        # return render(request, self.template, self.context)

class Success(View):
    template = "Test/success.html"
    context = {}
    def get(self, request):
        todoList = TodoList.objects.filter(user = request.user, compile = True)
        unCompleted = TodoList.objects.filter(user = request.user, compile = False)
        self.context |= ({
            'todoList': todoList,
            'unCompleted': unCompleted,
        })
        return render(request, self.template, self.context)
    def post(self, request):
        return render(request, self.template, self.context)

class Complete(View):
    template = "Test/success.html"
    context = {}
    def get(self, request):
        return render(request, self.template, self.context)
    def post(self, request):
        return render(request, self.template, self.context)

class Update(View):
    pass 

class Delete(View):
    pass 

class Logout(View):
    pass