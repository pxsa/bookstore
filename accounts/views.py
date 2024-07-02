from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.

class CreatUser(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')