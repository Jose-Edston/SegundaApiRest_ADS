from django.db import models


class Contatos(models.Model):    
    nome = models.CharField(max_length=255, null=True, blank=True)
    idade = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.idade}"

    class Meta:
        verbose_name_plural = "Contato"

