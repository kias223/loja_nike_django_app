# Generated by Django 4.1.6 on 2023-02-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0026_remove_product_props_data_lançamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_props',
            name='data_lançamento',
            field=models.DateField(null=True),
        ),
    ]
