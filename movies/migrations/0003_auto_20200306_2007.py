# Generated by Django 3.0.3 on 2020-03-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
