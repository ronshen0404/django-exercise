# Generated by Django 4.0.4 on 2022-06-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_book_slug1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug1',
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
