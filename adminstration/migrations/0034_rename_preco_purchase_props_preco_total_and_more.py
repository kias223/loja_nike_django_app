# Generated by Django 4.1.6 on 2023-03-13 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0033_alter_purchase_props_tamanho'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_props',
            old_name='preco',
            new_name='preco_total',
        ),
        migrations.RenameField(
            model_name='purchase_props',
            old_name='parcelas',
            new_name='valor_parcelas',
        ),
    ]
