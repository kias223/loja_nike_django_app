# Generated by Django 4.1 on 2023-02-01 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminstration', '0011_purchase_props_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_props',
            name='user_name',
        ),
    ]
