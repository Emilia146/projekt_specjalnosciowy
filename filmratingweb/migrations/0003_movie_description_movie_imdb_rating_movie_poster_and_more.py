# Generated by Django 4.1.5 on 2023-01-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmratingweb', '0002_movie_year_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='movie',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
    ]
