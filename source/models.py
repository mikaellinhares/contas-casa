from django.db import models


class Propriedade(models.Model):
    nome = models.CharField(max_length=50)
    pessoas = models.ManyToManyField('Pessoa')


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    nascimento = models.DateField(null=True)
    propriedades = models.ManyToManyField('Propriedade')


class Renda(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(max_length=255)


class Meta(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, null=True, blank=False)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(max_length=255)
    data_final = models.DateTimeField(null=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)
    cor = models.CharField(max_length=7)  # #FFFFFF


class Despesa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, null=True, blank=False)
    id_meta = models.ForeignKey(Meta, on_delete=models.CASCADE, null=True, blank=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField()


class Pagamento(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField()
