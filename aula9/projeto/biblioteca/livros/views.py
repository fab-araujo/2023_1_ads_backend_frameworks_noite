from django.shortcuts import render, redirect

from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    response = requests.get('https://araujofa.pythonanywhere.com/livros/')
    livros = response.json()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)

def adicionar(request):
    if request.method == "POST":
        dados = request.POST
        novo_livro = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"]
        }
        post_response = requests.post('https://araujofa.pythonanywhere.com/livros/', json=novo_livro)
        return redirect("index")

    context = {}
    return render(request, 'adicionar.html', context)