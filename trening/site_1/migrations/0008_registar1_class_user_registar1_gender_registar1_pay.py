# Generated by Django 4.2.5 on 2024-03-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registar1',
            name='class_user',
            field=models.CharField(choices=[('A', 'A  Motorcycles'), ('B', 'B  Car 3.500 kg '), ('C', 'C  Small truck 7.500 kg')], default='0000000', max_length=1),
        ),
        migrations.AddField(
            model_name='registar1',
            name='gender',
            field=models.CharField(choices=[('O', 'Other'), ('M', 'Male'), ('F', 'Female')], default='0000000', max_length=1),
        ),
        migrations.AddField(
            model_name='registar1',
            name='pay',
            field=models.CharField(choices=[('all', 'Pay all'), ('24', '24'), ('12', '12'), ('6', '6'), ('3', '3')], default='0000000', max_length=3),
        ),
    ]
