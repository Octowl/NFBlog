# Generated by Django 2.0.2 on 2018-03-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180305_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='location_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='website',
            field=models.URLField(),
        ),
    ]