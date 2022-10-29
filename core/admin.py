from django.contrib import admin

from .models import Cargo, Servico, Funcionario

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificados')
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'icone', 'ativo', 'modificados')
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificados')



# Register your models here.
