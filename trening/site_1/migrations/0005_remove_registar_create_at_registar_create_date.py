# Generated by Django 4.2.5 on 2024-03-23 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0004_alter_registar_passp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registar',
            name='create_at',
        ),
        migrations.AddField(
            model_name='registar',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
