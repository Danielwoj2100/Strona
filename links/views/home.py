from django.shortcuts import render
from django.views.generic import TemplateView
from random import randint
from links.models import Kurs


class homeView(TemplateView):

   template_name = 'home.html'
   def get_context_data(self, **kwargs):
      context = super(homeView, self).get_context_data(**kwargs)
      context['title'] = 'home'
      count = Kurs.objects.all().count()
      randomIndex = randint(0, count-1)
      context['kurs'] = Kurs.objects.all()[randomIndex]
      return context
   
   

 
