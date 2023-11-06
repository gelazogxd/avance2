from django.shortcuts import render
from django.views import generic

from .models import GrantGoal

# Create your views here.

class ListGrantGoal(generic.View):
    template_name = "core/gg_list.html"
    context = {}


# Se instancia la clase para poner atributos
    def get(self, request, *args, **kwargs):
        queryset = GrantGoal.objects.filter(status=True) #consulta que lleva where
        self.context = {
            "grant_goals" : queryset
        }
        return render(request, self.template_name, self.context)
    
    # def para consultar
    # get para obtener
