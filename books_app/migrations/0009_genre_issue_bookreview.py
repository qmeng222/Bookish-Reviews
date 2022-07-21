# Generated by Django 4.0.6 on 2022-07-21 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0008_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('issue_date', models.DateField()),
                ('description', models.TextField(null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('pages', models.SmallIntegerField(null=True)),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_issues', to='books_app.magazine')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='books_app.book')),
            ],
        ),
    ]