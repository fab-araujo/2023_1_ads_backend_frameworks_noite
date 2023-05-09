from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib import messages

from .models import Question, Choice

def index(request):
    questoes = Question.objects.all()
    context = {
        'questoes_template': questoes
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    questao = Question.objects.get(id=question_id)
    opcoes = Choice.objects.filter(question = question_id)
    context = {
        'pergunta': questao,
        'respostas': opcoes
    }
    return render(request, 'detail.html', context)

def results(request, question_id):
    questao = Question.objects.get(id=question_id)
    opcoes = Choice.objects.filter(question = question_id)
    context = {
        'pergunta': questao,
        'respostas': opcoes
    }
    return render(request, 'results.html', context)

def vote(request, question_id):
    if request.method == 'POST':
        post = request.POST
        opcao_votada = Choice.objects.get(id=post['voto'])
        opcao_votada.votes = opcao_votada.votes + 1
        opcao_votada.save()
        messages.success(request, 'Voto computado com sucesso.')
        return redirect("index")
    
    questao = Question.objects.get(id=question_id)
    opcoes = Choice.objects.filter(question = question_id)
    context = {
        'pergunta': questao,
        'respostas': opcoes
    }
    return render(request, 'vote.html', context)