from django.db import models

class Barbearia(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    horario_funcionamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome