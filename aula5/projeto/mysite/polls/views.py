from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)

def detail(request, question_id):
    context = {}
    return render(request, 'detail.html', context)

def results(request, question_id):
    context = {}
    return render(request, 'results.html', context)

def vote(request, question_id):
    context = {}
    return render(request, 'vote.html', context)