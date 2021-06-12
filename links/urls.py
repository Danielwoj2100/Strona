from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [    
    path('', login_required(views.homeView.as_view())),
    path('kursy/', login_required(views.listaKategoriiView.as_view())),
    path('kursy/<slug:slug>/', login_required(views.kursyDoKategoriiView.as_view())),
    path('kursy/<slug:kat>/<slug:kurs>', login_required(views.kursView.as_view())),
    path('new_user/', views.NewUserView.as_view()),
] 
