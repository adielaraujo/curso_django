from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    receber_noticia = models.BooleanField()
    mensagem_email = models.TextField()

    objects = models.Manager()

def __str__(self):
    return self.nome
