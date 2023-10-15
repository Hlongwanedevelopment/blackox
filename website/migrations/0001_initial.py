# Generated by Django 4.2.5 on 2023-09-30 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(blank=True, max_length=500, null=True)),
                ('description_of_breed', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telephone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Sheep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(blank=True)),
                ('image', models.ImageField(upload_to='sheep/')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('stock', models.BooleanField(default=False)),
                ('breed_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.breed')),
            ],
            options={
                'ordering': ['-Age'],
            },
        ),
        migrations.CreateModel(
            name='Cattle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(blank=True)),
                ('image', models.ImageField(upload_to='cattles/')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('stock', models.BooleanField(default=False)),
                ('breed_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.breed')),
            ],
            options={
                'ordering': ['-Age'],
            },
        ),
    ]
