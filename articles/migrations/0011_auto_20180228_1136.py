# Generated by Django 2.0.2 on 2018-02-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_team_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]