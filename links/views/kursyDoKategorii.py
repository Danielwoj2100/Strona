from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from links.models import Kategoria, Kurs

class kursyDoKategoriiView(TemplateView):

    template_name = 'kursyDoKategorii.html'
    def get_context_data(self, **kwargs):
        context = super(kursyDoKategoriiView, self).get_context_data(**kwargs)

        kat = self.kwargs['slug']
        kategoria = Kategoria.objects.get(nazwa_kategorii=kat)


        kursy = Kurs.objects.filter(kategoria=kategoria.id)
        context['title'] = 'kursy'
        context['kursy'] = kursy
        context['kategoria'] = kat
        return context
    
 