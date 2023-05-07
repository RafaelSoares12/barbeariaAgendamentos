from django import forms
from django.forms import DateField, NumberInput, Select, TimeField

from agendamentos.models import Reserva, Servico


class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ['cliente', 'barbearia', 'data', 'hora', 'servico']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'barbearia': forms.TextInput(attrs={'class': 'form-control'}),
            'data': DateField(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'hora': TimeField(format='%H:%M', attrs={'class': 'form-control'}),
            'cadeiras_reservadas': NumberInput(attrs={'class': 'form-control'}),
            'servico': Select(attrs={'class': 'form-control'}),
        }

    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), empty_label=None)
