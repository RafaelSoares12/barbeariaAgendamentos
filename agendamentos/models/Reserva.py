from django.db import models
from agendamentos.models import Cliente, Barbearia
from agendamentos.models.Servico import Servico

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.cliente
