# Generated by Django 3.1.5 on 2021-06-30 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.productcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 20, 14, 26, 105486)),
        ),
    ]
