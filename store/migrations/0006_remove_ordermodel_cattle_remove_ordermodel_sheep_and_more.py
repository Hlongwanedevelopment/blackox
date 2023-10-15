# Generated by Django 4.2.5 on 2023-10-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_item_cattle_item_sheep_alter_item_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='cattle',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='sheep',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
