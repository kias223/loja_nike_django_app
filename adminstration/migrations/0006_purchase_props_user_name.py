# Generated by Django 4.1 on 2023-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0005_alter_purchase_props_purchase_img_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_props',
            name='user_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
