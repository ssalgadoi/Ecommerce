# Generated by Django 5.0.7 on 2024-07-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]