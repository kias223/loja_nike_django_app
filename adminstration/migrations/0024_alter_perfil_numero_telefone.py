# Generated by Django 4.1.6 on 2023-02-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0023_alter_perfil_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='numero_telefone',
            field=models.CharField(max_length=14, null=True),
        ),
    ]