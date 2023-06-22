from django.contrib import admin

from contatos.models import Contatos


@admin.register(Contatos)
class ContatosAdmin(admin.ModelAdmin):
    exclude = ()

