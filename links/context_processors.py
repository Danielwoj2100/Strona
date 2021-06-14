def categories(request):
    from links.models import Kategoria

    return {
        'categories': Kategoria.objects.all(),  
    } 
