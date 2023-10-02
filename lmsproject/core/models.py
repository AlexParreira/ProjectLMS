from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from  embed_video.fields  import  EmbedVideoField
import random

def generate_unique_id():
    """
    Função para gerar IDs únicos com 8 dígitos.
    """
    while True:
        unique_id = random.randint(10000000, 99999999)  # Gera um número aleatório com 8 dígitos
        if not Curso.objects.filter(id=unique_id).exists():  # Verifica se o ID já existe no banco de dados
            return unique_id

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ultima_vez_logado = models.DateTimeField(null=True, blank=True)
    tempo_logado = models.DurationField(null=True, blank=True)
    cursos_liberados = models.ManyToManyField('Curso', blank=True)

    def __str__(self):
        return self.user.username

class Curso(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=255)
    itens_conteudo = models.ManyToManyField('ItemConteudo', blank=True)

    def __str__(self):
        return self.titulo

class ItemConteudo(models.Model):
    id = models.AutoField(primary_key=True)
    subtitulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='curso_imagens/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    video = EmbedVideoField(blank=True,null=True)

    def __str__(self):
        return self.subtitulo

# Conecte um sinal para gerar IDs únicos antes de salvar
@receiver(pre_save, sender=Curso)
def generate_id(sender, instance, **kwargs):
    if not instance.id:
        instance.id = generate_unique_id()