# Generated by Django 4.0.6 on 2022-07-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0010_delete_bookreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='genre',
            field=models.ManyToManyField(related_name='magazines', to='books_app.genre'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]