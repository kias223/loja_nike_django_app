# Generated by Django 4.1 on 2023-02-01 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminstration', '0008_rename_user_name_purchase_props_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_props',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
