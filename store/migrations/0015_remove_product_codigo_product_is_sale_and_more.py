# Generated by Django 5.0.7 on 2024-07-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='codigo',
        ),
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
