# Generated by Django 2.0.2 on 2018-03-14 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20180311_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name_plural': 'people'},
        ),
    ]
