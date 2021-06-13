from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views


urlpatterns = [    
    path('', views.homeView.as_view()),
    path('kursy/', views.listaKategoriiView.as_view()),
    path('kursy/<slug:slug>/', views.kursyDoKategoriiView.as_view()),
    path('kursy/<slug:kat>/<slug:kurs>', views.kursView.as_view()),
    path('new_user/', views.NewUserView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
] 
