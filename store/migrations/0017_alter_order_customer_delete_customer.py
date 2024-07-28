# Generated by Django 5.0.7 on 2024-07-28 02:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('store', '0016_alter_product_is_sale_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer', verbose_name='Cliente'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]