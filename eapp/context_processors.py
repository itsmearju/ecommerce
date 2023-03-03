from . models import Category

#------saving all links of category menu ----#

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)         #--converting to dictionary---#