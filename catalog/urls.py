from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('Pots', views.potFilterView.as_view(), name='Pots'),
    url('Decor', views.decorFilterView.as_view(), name='Decor'),
    url('Dishes', views.dishesFilterView.as_view(), name='Dishes'),
    url(r'^Pot/(?P<pk>\d+)$', views.potDetailView.as_view(), name='Pot-detail'),
    url(r'^Dec/(?P<pk>\d+)$', views.decDetailView.as_view(), name='Decor-detail'),
    url(r'^Dish/(?P<pk>\d+)$', views.dishDetailView.as_view(), name='Dish-detail'),
    url(r'^article/(?P<pk>\d+)$', views.articleDetailView.as_view(), name='article-detail'),
    url('Architecture', views.architectureListView.as_view(), name='Architecture'),
    url('Design', views.designListView.as_view(), name='Design'),
    url('Culture', views.cultureListView.as_view(), name='Culture'),
    url('Contacts', views.contacts, name='Contacts'),
    url('About', views.about, name='About'),
    url(r'^author/(?P<pk>\d+)$', views.authorDetailView.as_view(), name='author-detail'),
]
