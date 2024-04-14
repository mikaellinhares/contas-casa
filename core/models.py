from django.db import models


class Propriedade(models.Model):
    nome = models.CharField(max_length=50)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    nascimento = models.DateField(null=True)


class PropriedadePessoa(models.Model):
    id_propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)


class Renda(models.Model):
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(max_length=255)


class Meta(models.Model):
    id_propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(max_length=255)
    data_final = models.DateTimeField(null=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)
    cor = models.CharField(max_length=7)  # #FFFFFF


class Despesa(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    id_meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField()


class Pagamento(models.Model):
    id_despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField()
