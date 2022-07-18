# Generated by Django 4.0.6 on 2022-07-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('author', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('book_cover_url', models.URLField(blank=True, null=True)),
                ('is_in_print', models.BooleanField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
