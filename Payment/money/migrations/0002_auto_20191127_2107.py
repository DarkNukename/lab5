# Generated by Django 2.2.5 on 2019-11-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylist',
            name='coeff',
            field=models.CharField(max_length=6),
        ),
    ]
