from django.db import models
import math



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observaces = models.TextField()
    def __str__(self):
        return str(self.marca) + '-'+ self.placa + ' do Sr(a):' + str(self.proprietario)
    

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return 'Parâmentros gerais'
    
    
    

class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return str(self.veiculo)

    def horas_total(self):
        total_segundos = (self.checkout - self.checkin).total_seconds()
        total_horas = math.ceil(total_segundos/3600)
        return total_horas

    def total(self):
        return self.valor_hora * self.horas_total()

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo+' - '+self.inicio) 

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pagto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        return str(self.mensalista) +' - '+ str(self.total)
    
