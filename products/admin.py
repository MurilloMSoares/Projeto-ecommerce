from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque')
    list_filter = ('categoria',)
    search_fields = ('nome',)