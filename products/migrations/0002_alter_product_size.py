# Generated by Django 4.0.3 on 2022-04-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='product_size', to='products.size'),
        ),
    ]