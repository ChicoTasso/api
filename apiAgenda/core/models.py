from django.db import models

# Create your models here.


class Agenda(models.Model):
     
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email', blank=True, null=True)

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'