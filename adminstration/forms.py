from .models import product_props, perfil, purchase_props
from django import forms

class Postform(forms.ModelForm):
    class Meta:
        model = product_props
        fields = ('modelo',
                  'preço',
                  'desconto',
                  'parcelas',
                  'img_produto',
                  'tamanho35',
                  'tamanho36',
                  'tamanho37',
                  'tamanho38',
                  'tamanho39',
                  'tamanho40',
                  'tamanho41',
                  'tamanho42',
                  'tamanho43',
                  'tamanho44',
                  'tamanho45',
                  'data_lançamento',
                  )

class userform(forms.ModelForm):
    class Meta:
        model = perfil
        fields = (
        'nome_completo',
        'cpf',
        'rua',
        'bairro',
        'numero_casa',
        'cep',
        'numero_telefone',
        )

class purchaseform(forms.ModelForm):
    class Meta:
        model = purchase_props
        fields = (
            'status',
        )


