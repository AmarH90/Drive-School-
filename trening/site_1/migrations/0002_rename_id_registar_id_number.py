# Generated by Django 4.2.5 on 2024-03-23 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registar',
            old_name='id',
            new_name='id_number',
        ),
    ]
