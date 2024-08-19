from django.shortcuts import render
from .models import Bb, Rubric


# Create your views here.

# def index(request):
#     bbs = Bb.objects.all()
#     return render(request, 'bboard/index.html', {'bbs': bbs})


def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)
