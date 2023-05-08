# Generated by Django 4.1 on 2023-02-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0016_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='bairro',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nome_completo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero_casa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero_telefone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rua',
            field=models.CharField(max_length=30, null=True),
        ),
    ]