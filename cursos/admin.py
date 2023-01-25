from django.contrib import admin

from .models import Materia, Avaliacao


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('materia', 'url', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('materia', 'nome', 'email', 'nota', 'atualizacao', 'ativo')
