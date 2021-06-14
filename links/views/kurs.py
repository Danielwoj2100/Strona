from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from links.models import Kategoria, Kurs, Film

class kursView(TemplateView):

    template_name = 'kurs.html'
    def get_context_data(self, **kwargs):
        context = super(kursView, self).get_context_data(**kwargs)

        kat = self.kwargs['kat']
        kurs = self.kwargs['kurs']
        
        kategoria = Kategoria.objects.get(nazwa_kategorii=kat)
        kurs_nazwa = Kurs.objects.get(nazwa=kurs)
        
        print(kurs_nazwa)
        
        filmy = Film.objects.filter(kurs=kurs_nazwa)
        
        for film in filmy:
            if 'watch?v=' in film.hiperlacze:
                string = film.hiperlacze
                film.hiperlacze = string.replace("watch?v=", "embed/")
                film.save()
        
        context['title'] = 'kurs'
        context['filmy'] = filmy
        context['kurs'] = kurs

        return context 
