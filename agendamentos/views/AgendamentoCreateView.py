from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from agendamentos.models import Reserva
from agendamentos.forms import ReservaForm

class AgendamentoCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    # template_name = 
    # success_url = 

    def form_valid(self, form):
        return super().form_valid(form)
