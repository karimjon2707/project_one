from .models import Category


def menu_links(request):
    maxsulot_tur = Category.objects.all()
    context = {
        "maxsulot_all": maxsulot_tur
    }
    return dict(context)
