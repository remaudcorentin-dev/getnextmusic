
from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    context={}
    return render(request, "index.html", context=context)
