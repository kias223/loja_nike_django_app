from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class product_props(models.Model):
    modelo = models.CharField(max_length=200)
    preço = models.CharField(max_length=8)
    tamanho35 = models.BooleanField('tamanho35', default=False)
    tamanho36 = models.BooleanField('tamanho36', default=False)
    tamanho37 = models.BooleanField('tamanho37', default=False)
    tamanho38 = models.BooleanField('tamanho38', default=False)
    tamanho39 = models.BooleanField('tamanho39', default=False)
    tamanho40 = models.BooleanField('tamanho40', default=False)
    tamanho41 = models.BooleanField('tamanho41', default=False)
    tamanho42 = models.BooleanField('tamanho42', default=False)
    tamanho43 = models.BooleanField('tamanho43', default=False)
    tamanho44 = models.BooleanField('tamanho44', default=False)
    tamanho45 = models.BooleanField('tamanho45', default=False)
    desconto = models.IntegerField(default=0)
    parcelas = models.IntegerField(default=0)
    img_produto = models.ImageField(
        upload_to='img_produto/', null=True, blank=True)
    data_lançamento = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('adminstration-view')


class purchase_props(models.Model):
    status_choices = (
        ('pagamento confirmado', 'pagamento confirmado'),
        ('preparando produto para entrega', 'preparando produto para entrega'),
        ('produto em rota', 'produto em rota'),
        ('produto entregue', 'produto entregue'),
    )

    tamanho = models.CharField(max_length=300)
    img_url = models.CharField(max_length=3000)
    modelo = models.CharField(max_length=3000)
    modelo_id = models.CharField(max_length=500)
    preco_total = models.CharField(max_length=100)
    valor_parcelas = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    status = models.CharField(choices=status_choices,
                              null=True, blank=True, max_length=100)
    data_hora = models.CharField(max_length=50, null=True, blank=True)


class perfil(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=14, null=True)
    cep = models.CharField(max_length=9, null=True)
    rua = models.CharField(max_length=30, null=True)
    bairro = models.CharField(max_length=30, null=True)
    numero_casa = models.IntegerField(null=True)
    numero_telefone = models.CharField(max_length=14, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
