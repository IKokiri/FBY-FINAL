# Generated by Django 3.0.6 on 2020-06-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=200)),
            ],
        ),
    ]