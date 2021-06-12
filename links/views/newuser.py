from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.db import connections 
from django.db import transaction


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

class NewUserView(TemplateView):
    template_name = 'newuser.html'


    def get_context_data(self, **kwargs):
        context = super(NewUserView, self).get_context_data(**kwargs)
        context['title'] = 'new'
        return context
	
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email,password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
           
		
        return redirect('/')


   
