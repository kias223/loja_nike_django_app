# Generated by Django 4.1 on 2022-12-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_props',
            name='img_produto',
            field=models.ImageField(upload_to='img_produto/'),
        ),
    ]