from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class homeView(TemplateView):

   template_name = 'home.html'
   def get_context_data(self, **kwargs):
      context = super(homeView, self).get_context_data(**kwargs)
      context['title'] = 'home'
      return context
   
   

 
