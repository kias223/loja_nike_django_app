from adminstration.models import purchase_props
from django import forms


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = purchase_props
        fields = (
            'tamanho',
            'img_url',
            'modelo',
            'modelo_id',
            'preco_total',
            'valor_parcelas',
            'quantidade',
            'user_name',
            'user_id',
            'data_hora',
        )
