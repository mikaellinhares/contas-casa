from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def nascimento_padrao(self) -> str:
        return '-'.join(reversed(str(self.nascimento).split('/')))


class Propriedade(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=75, null=True)
    imagem = models.ImageField(upload_to='propriedades', null=True);
    pessoas = models.ManyToManyField(Pessoa)

    def __str__(self):
        return self.nome


class Renda(models.Model):
    nome = models.TextField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.pessoa} - R${self.valor}'


class Meta(models.Model):
    nome = models.CharField(max_length=100)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - R${self.saldo}/R${self.valor}'


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    cor = models.CharField(max_length=7)  # #FFFFFF

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE, null=True, blank=True)
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateField()
    vencimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - R${self.valor}'


class Pagamento(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    data = models.DateTimeField()

    def __str__(self):
        return f'{self.pessoa} - {self.despesa} - R${self.valor}'
