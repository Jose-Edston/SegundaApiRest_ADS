from django.urls import include, path
from rest_framework import routers

from contatos.views import ContatosViewSet

router = routers.DefaultRouter()

router.register(r'contato', ContatosViewSet)

urlpatterns = [
    path("", include(router.urls)),
]