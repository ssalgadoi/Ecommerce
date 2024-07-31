# Generated by Django 5.0.7 on 2024-07-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_order_date_shipped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='shipping_address2',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de envío'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False, verbose_name='Enviado'),
        ),
    ]
