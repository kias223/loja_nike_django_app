# Generated by Django 4.1 on 2022-12-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_props',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('preço', models.CharField(max_length=8)),
                ('tamanho35', models.BooleanField(default=False, verbose_name='tamanho35')),
                ('tamanho36', models.BooleanField(default=False, verbose_name='tamanho36')),
                ('tamanho37', models.BooleanField(default=False, verbose_name='tamanho37')),
                ('tamanho38', models.BooleanField(default=False, verbose_name='tamanho38')),
                ('tamanho39', models.BooleanField(default=False, verbose_name='tamanho39')),
                ('tamanho40', models.BooleanField(default=False, verbose_name='tamanho40')),
                ('tamanho41', models.BooleanField(default=False, verbose_name='tamanho41')),
                ('tamanho42', models.BooleanField(default=False, verbose_name='tamanho42')),
                ('tamanho43', models.BooleanField(default=False, verbose_name='tamanho43')),
                ('tamanho44', models.BooleanField(default=False, verbose_name='tamanho44')),
                ('tamanho45', models.BooleanField(default=False, verbose_name='tamanho45')),
                ('desconto', models.IntegerField(default=0)),
                ('parcelas', models.IntegerField(default=0)),
                ('img_produto', models.ImageField(upload_to='img_produto')),
            ],
        ),
    ]
