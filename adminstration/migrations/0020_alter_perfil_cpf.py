# Generated by Django 4.1.6 on 2023-02-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0019_purchase_props_purchase_modelo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
