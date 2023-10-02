from django.contrib import admin
from .models import Aluno, Curso, ItemConteudo




class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
admin.site.register(Curso, CursoAdmin)
class ItemConteudoAdmin(admin.ModelAdmin):
    list_display = ('id', 'subtitulo')
admin.site.register(ItemConteudo, ItemConteudoAdmin)


# Registre o modelo Aluno sem criar uma classe personalizada para ele
admin.site.register(Aluno)

