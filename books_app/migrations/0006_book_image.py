# Generated by Django 4.0.6 on 2022-07-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0005_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
