# Generated by Django 4.2.5 on 2024-03-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('b_year', models.CharField(max_length=20)),
                ('card_id', models.CharField(max_length=50)),
                ('passp', models.ImageField(upload_to='img-library')),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
