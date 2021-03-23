from .models import pot, dishes, decor, material
import django_filters
from django import forms

class potFilter(django_filters.FilterSet):
    material = django_filters.ModelMultipleChoiceFilter(queryset=material.objects.all(),
    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = pot
        fields = [ 'material']

class dishesFilter(django_filters.FilterSet):
    material = django_filters.ModelMultipleChoiceFilter(queryset=material.objects.all(),
    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = dishes
        fields = [ 'material']

class decorFilter(django_filters.FilterSet):
    material = django_filters.ModelMultipleChoiceFilter(queryset=material.objects.all(),
    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = decor
        fields = [ 'material']