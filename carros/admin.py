from django.contrib import admin
from carros.models import Carro 

class Carros(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano')
    list_display_links = ('modelo', 'marca', 'ano')



admin.site.register(Carro, Carros)