from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class material(models.Model):
    """
    Модель материал
    """
    name = models.CharField(max_length=20, help_text="ВВедите материал")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('material-detail', args=[str(self.id)])
    
class color(models.Model):
    """
    Модель Цвет
    """
    name = models.CharField(max_length=20, help_text="ВВедите цвет")

    def __str__(self):
        return self.name

class style(models.Model):
    """
    Модель стиль
    """
    name = models.CharField(max_length=20, help_text="ВВедите стиль")

    def __str__(self):
        return self.name

class size(models.Model):
    """
    Модель размер
    """
    name = models.CharField(max_length=20, help_text="ВВедите размер")

    def __str__(self):
        return self.name
    
class pot(models.Model):

    title = models.CharField(max_length=200)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    #ForeignKey потому что, один горшок имеет один материал, но из одного материала может быть множество горшков.
    summary = models.TextField(max_length=1000, help_text="Описание")
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    style = models.ManyToManyField(style, help_text="Стиль")
    #ManyToMany потому что, один горшок может быть исполнен в нескольких стилях.

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Pot-detail', args=[str(self.id)])

class dishes(models.Model):

    title = models.CharField(max_length=200)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Описание")
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    style = models.ManyToManyField(style, help_text="Стиль")
    kind = models.CharField(default='Посуда', max_length=200)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Dish-detail', args=[str(self.id)])

class decor(models.Model):

    title = models.CharField(max_length=200)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Описание")
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    style = models.ManyToManyField(style, help_text="Стиль")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Decor-detail', args=[str(self.id)])

class author(models.Model):

    nickname = models.CharField(max_length=50)
    about = models.TextField(max_length=200)

    def __str__(self):
        return self.nickname
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
class article(models.Model):

    title = models.CharField(max_length=200)
    author = models.ManyToManyField(author)
    pub_date = models.DateField()
    text = RichTextField(blank = True, null = True)
    summary = models.TextField(max_length=200)
    theme = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])    

      
