# Generated by Django 3.1.1 on 2021-03-17 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20210317_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'managed': False},
        ),
    ]
