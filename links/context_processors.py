def categories(request):
    from links.models import Kategoria
    categories = Kategoria.objects.all()

    return {
        'categories': categories,  
    } 
