# Generated by Django 3.0.6 on 2020-06-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagar', '0006_auto_20200609_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagar',
            name='tag',
            field=models.CharField(default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='pagar',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
    ]
