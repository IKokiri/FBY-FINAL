# Generated by Django 3.0.6 on 2020-06-08 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classificacao', '0001_initial'),
        ('pagar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagar',
            name='classificacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classificacao.Classificacao'),
        ),
    ]