from livros.apps import LivrosConfig
from django.http.response import HttpResponse
from .models import Livro

def livros_view(request):
    livros = Livro.objects.all()
    output = [{
        'nome': livros.nome,
        'categoria': livros.categoria,
        'autor': livros.autor
    } for livro in  livros]

    return HttpResponse(str(output))

