from django.db import models

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True, null=False, unique=True)
    tipo = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.referencia 

    class Meta:
        db_table = 'produto' 



class VendaMaster(models.Model):
    codigo = models.AutoField(primary_key=True, null=False, unique=True)
    cpf_nota = models.CharField(max_length=11)
    troco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dinheiro = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.codigo}: {self.total}"
    
    class Meta:
        db_table = 'vendas_master'



class VendaDetalhe(models.Model):
    codigo = models.AutoField(primary_key=True, null=False, unique=True)
    qtd = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    qtd_devolvida = models.IntegerField(default=0)

    class Meta:
        db_table = 'vendas_detalhe'

    def __str__(self):
        return f"VendaDetalhe {self.codigo}: {self.total}"
    



class Pessoa(models.Model):
    codigo = models.AutoField(primary_key=True, null=False, unique=True)
    empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)
    email1 = models.EmailField(max_length=255, unique=True)
    celular1 = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'pessoa'

    def __str__(self):
        return f"{self.empresa} - {self.cnpj}"

