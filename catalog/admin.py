from django.contrib import admin

# Register your models here.

from .models import size, style, color, material, pot, dishes, decor, article, author

admin.site.register(size)
admin.site.register(style)
admin.site.register(color)

@admin.register(author)
class articlesAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'about')

@admin.register(article)
class articlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme')
    list_filter = ('title', 'theme')

@admin.register(dishes)
class dishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity')
    list_filter = ('title', 'price', 'quantity')

@admin.register(pot)
class potAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity')
    list_filter = ('title', 'price', 'quantity')

@admin.register(decor)
class decorAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity')
    list_filter = ('title', 'price', 'quantity')

class potInline(admin.TabularInline):
    model = pot
    exclude = ['summary', 'style']

class decorInline(admin.TabularInline):
    model = decor
    exclude = ['summary', 'style']

class dishesInline(admin.TabularInline):
    model = dishes
    exclude = ['summary', 'style', 'type']

class articlesInline(admin.TabularInline):
    model = article
    exclude = ['title', 'theme']
    
@admin.register(material)
class materialAdmin(admin.ModelAdmin):
    inlines = [potInline, dishesInline, decorInline]
