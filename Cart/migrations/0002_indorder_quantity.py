# Generated by Django 4.1.1 on 2024-02-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indorder',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]