from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Criar class que representa a entidade e seus atributos no BD
class Evento(models.Model):
    # nome do atributo = tipo do atribuito()
    nome =  models.CharField(verbose_name='nome', max_length=100, null=True)
    local = models.CharField(verbose_name='local', max_length=100, null=True)
    data= models.DateField(verbose_name='data', null=True )
    horario= models.TimeField(verbose_name='horario', null=True)
    descricao = models.TextField(verbose_name='descricao', null=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )