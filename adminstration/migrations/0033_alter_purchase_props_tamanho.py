# Generated by Django 4.1.6 on 2023-03-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0032_rename_purchase_img_produto_purchase_props_img_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_props',
            name='tamanho',
            field=models.CharField(max_length=30),
        ),
    ]
