# Generated by Django 2.2.5 on 2019-10-18 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ate_employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ate_employees',
            name='id',
        ),
        migrations.AddField(
            model_name='ate_employees',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
