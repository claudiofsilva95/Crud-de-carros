from django.db import models


class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100)
    tipo_do_combustivel = models.CharField(max_length=100, verbose_name='Tipo do combustivel')
    portas = models.CharField(max_length=100)
    transmissao = models.CharField(max_length=100, verbose_name='Transmissão')
    motor = models.CharField(max_length=100)
    tipo_da_carroceria = models.CharField(max_length=100, verbose_name='Tipo da carroceria')
    km = models.CharField(max_length=100, verbose_name='Quilômetros')

    def __str__(self):
        return self.modelo

        