# Generated by Django 4.2.6 on 2023-11-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_point', '0012_remove_product_price_product_stripe_product_id_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
