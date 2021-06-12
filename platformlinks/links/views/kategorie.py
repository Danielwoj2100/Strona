from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from links.models import Kategoria

class listaKategoriiView(TemplateView):

    template_name = 'kategorie.html'
    def get_context_data(self, **kwargs):
        context = super(listaKategoriiView, self).get_context_data(**kwargs)

        kategorie = Kategoria.objects.all()
        # kategorie = Kategoria.objects.values_list('nazwa_kategorii').distinct()
                    # models.Shop.objects.order_by().values('city').distinct()
        
        print(type(kategorie[0]))
        
        context['title'] = 'kursy'
        context['kategorie'] = kategorie

        return context
