from .serializers import LivrosSerializer
from django.db.models import query
from rest_framework import serializers, views, viewsets
from .models import Livro


class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livro.objects.all()
     







"""
******************************************************************************
Opção 1 
******************************************************************************
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

"""




"""
******************************************************************************
Opção 2
******************************************************************************
class LivrosApiView(APIView):
    def get(self, request):
        livros = Livro.objects.all()
        output = [{
        'nome': livro.nome,
        'categoria': livro.categoria,
        'autor': livro.autor
        } for livro in  livros]

        return Response(output)

    def post(self, request):
        livro = Livro.objects.create(nome=request.data.get('nome'),
                                    categoria=request.data.get('categoria'),
                                    autor=request.data.get('autor'))
        output = [{
            'nome': livro.nome,
            'categoria': livro.categoria,
            'autor': livro.autor
        }]

        return Response(output)
"""