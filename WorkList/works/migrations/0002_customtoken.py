# Generated by Django 2.2.5 on 2019-12-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=40, verbose_name='Token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
        ),
    ]