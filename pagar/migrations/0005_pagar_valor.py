# Generated by Django 3.0.6 on 2020-06-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagar', '0004_auto_20200609_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagar',
            name='valor',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
