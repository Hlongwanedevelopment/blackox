# Generated by Django 4.2.5 on 2023-10-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hearder_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title_tag', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('Category', models.CharField(max_length=50)),
                ('Snippet', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
