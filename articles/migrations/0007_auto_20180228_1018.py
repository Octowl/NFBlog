# Generated by Django 2.0.2 on 2018-02-28 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20180227_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-name']},
        ),
    ]