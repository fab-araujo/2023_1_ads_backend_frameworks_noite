from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from .models import Post, Comentario

import datetime
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts_template': posts
    }
    return render(request, 'index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comentarios = Comentario.objects.filter(post_id = post_id)
    context = {
        'post': post,
        'comentarios': comentarios
    }
    if request.method == 'POST':
        dados = request.POST
        comentario = Comentario(post_id = post, texto = dados['comentario'], com_date = datetime.datetime.now())
        comentario.save()
        messages.success(request, 'Comentario efetuado.')
        return redirect("index")
    return render(request, 'detail.html', context)