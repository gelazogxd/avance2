from django.shortcuts import render
from django.views import generic

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Gerardo Aguilar",
            "lista": [1, 2, 3]

        }
        return render(request, self.template_name, self.context)
    


    


# Ahorrador de html

class About(generic.View):
    template_name = "home/about.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Gerardo Aguilar"
        }
        return render(request, self.template_name, self.context)
    


class Identity(generic.View):
    template_name = "home/identity.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Gerardo Aguilar"
        }
        return render(request, self.template_name, self.context)
    



class Contacto(generic.View):
    template_name = "home/contacto.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Gerardo Aguilar"
        }
        return render(request, self.template_name, self.context)
    

