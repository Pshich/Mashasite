from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView
from .filter import potFilter, decorFilter, dishesFilter
# Create your views here.

from .models import size, style, color, material, pot, dishes, decor, author, article, author

def index(request):

    return render(request,'index.html', context={})

def contacts(request):

    return render(
        request,
        'Contacts.html',
        context={})

def about(request):

    return render(
        request,
        'About.html',
        context={})

class potFilterView(FilterView):
    model = pot
    filterset_class = potFilter # ADD YOUR filterset class
    template_name = 'catalog/pot_filter.html'
        
class decorFilterView(FilterView):
    model = decor
    filterset_class = decorFilter
    
class dishesFilterView(FilterView):
    model = dishes
    filterset_class = dishesFilter

class potDetailView(generic.DetailView):
    model = pot

class decDetailView(generic.DetailView):
    model = decor

class dishDetailView(generic.DetailView):
    model = dishes
    
class articleDetailView(generic.DetailView):
    model = article

class architectureListView(generic.ListView):
    queryset = article.objects.filter(theme = 'Архитектура')
    template_name = 'catalog/architecture.html'

class designListView(generic.ListView):
    queryset = article.objects.filter(theme = 'Дизайн')
    template_name = 'catalog/design.html'

class cultureListView(generic.ListView):
    model = article
    queryset = article.objects.filter(theme = 'Культура')
    template_name = 'catalog/culture.html'

class authorDetailView(generic.DetailView):
    model = author