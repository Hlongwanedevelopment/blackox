# Generated by Django 4.2.5 on 2023-10-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_ordermodel_cattle_remove_ordermodel_sheep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]