from django import urls
from livros.models import Livro
from rest_framework.routers import DefaultRouter

from .views import LivrosViewSet

router = DefaultRouter()
router.register(r'', LivrosViewSet)

livros_urls = router.urls 
