# Generated by Django 2.2.5 on 2019-10-18 19:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkList',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nps_name', models.CharField(max_length=30)),
                ('english_level', models.CharField(choices=[('0', 'отсутствует'), ('1', 'a1'), ('2', 'a2'), ('3', 'b1'), ('4', 'b2'), ('5', 'c1'), ('6', 'c2')], max_length=1)),
                ('specialization', models.CharField(choices=[('0', 'Монтажник'), ('1', 'Физик'), ('2', 'Технолог'), ('3', 'Программист'), ('4', 'Ядерщик'), ('5', 'КИП'), ('6', 'Электрик')], max_length=1)),
                ('skill', models.CharField(choices=[('0', 'Стажер'), ('1', '1я категория'), ('2', '2я категория'), ('3', '3я категория'), ('4', 'Ведущий')], max_length=1)),
                ('sum', models.IntegerField()),
            ],
        ),
    ]
