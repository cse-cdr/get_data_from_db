from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.db.models import Q
# Create your views here.
def index(request):
    return HttpResponse('hi world!')

def detail(request):
    question_obj = Question.objects.get(id=1)
    template = loader.get_template('detail.html')
    context = {'question_obj': question_obj}
    return HttpResponse(template.render(context,request))