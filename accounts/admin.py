from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario

    list_display = ('email', 'nome', 'sobrenome', 'is_staff')
    search_fields = ('email', 'nome', 'sobrenome')
    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        ('Dados pessoais', {
            'fields': ('nome', 'sobrenome')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Dados pessoais', {
            'fields': ('email', 'nome', 'sobrenome')
        }),
    )