from django.shortcuts import render
from .models import Food

# Create your views here.
def Show(request):
    posts=Food.objects.all()
    return  render(request,'webs/index.html',{'posts':posts})