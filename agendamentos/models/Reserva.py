from django.db import models
from agendamentos.models import Cliente, Barbearia

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    cadeiras_reservadas = models.IntegerField()