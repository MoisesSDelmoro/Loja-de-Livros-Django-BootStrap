from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Livro

@api_view(['GET', 'POST'])
def livros_view(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        output = [{
            'nome': livro.nome,
            'categoria': livro.categoria,
            'autor': livro.autor
        } for livro in  livros]
    elif request.method == 'POST':
        livro = Livro.objects.create(nome=request.data.get('nome'),
                                    categoria=request.data.get('categoria'),
                                    autor=request.data.get('autor'))
        output = [{
            'nome': livro.nome,
            'categoria': livro.categoria,
            'autor': livro.autor
        }]

    return Response(output)

