# Generated by Django 4.1.6 on 2023-03-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0034_rename_preco_purchase_props_preco_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_props',
            name='img_url',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='purchase_props',
            name='modelo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='purchase_props',
            name='modelo_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase_props',
            name='tamanho',
            field=models.CharField(max_length=100),
        ),
    ]
