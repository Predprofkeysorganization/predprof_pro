# Generated by Django 5.1.4 on 2025-01-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_inventory_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product_status',
            field=models.CharField(choices=[('сломанный', 'сломанный'), ('новый', 'новый'), ('используемый', 'используемый')], default='новый', max_length=12),
        ),
    ]