# Generated by Django 4.1.1 on 2024-02-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0003_delete_product_delete_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='ownerId',
            new_name='shopId',
        ),
        migrations.AddField(
            model_name='owner',
            name='shopName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]