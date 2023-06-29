# Generated by Django 4.1.5 on 2023-02-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmratingweb', '0004_additional_inf_movie_additional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional_inf',
            name='species',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (0, 'Inne'), (4, 'Drama'), (3, 'Sci-fi'), (2, 'Komedia')], default=0),
        ),
    ]