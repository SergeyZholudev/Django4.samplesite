from django.shortcuts import render
from .models import Bb


# Create your views here.

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})
