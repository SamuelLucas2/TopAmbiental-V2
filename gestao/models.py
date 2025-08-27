from django.db import models

class Cliente(models.Model):
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, help_text="Formato: XX.XXX.XXX/XXXX-XX")
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome_empresa

class Documento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='documentos')
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo