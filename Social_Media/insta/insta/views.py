from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy


def hello(request):
    return HttpResponse("<h1>You Forgot Your Password??? <br>Shame On You.</h1>")

def home(request):
    return render(request,'home.html')

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"