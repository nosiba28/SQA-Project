# Generated by Django 4.1.1 on 2024-02-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
