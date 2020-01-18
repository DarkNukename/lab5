# Generated by Django 2.2.5 on 2019-10-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ATE_Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('english_level', models.CharField(choices=[('0', 'отсутствует'), ('1', 'a1'), ('2', 'a2'), ('3', 'b1'), ('4', 'b2'), ('5', 'c1'), ('6', 'c2')], max_length=1)),
                ('specialization', models.CharField(choices=[('0', 'Монтажник'), ('1', 'Физик'), ('2', 'Технолог'), ('3', 'Программист'), ('4', 'Ядерщик'), ('5', 'КИП'), ('6', 'Электрик')], max_length=1)),
                ('skill', models.CharField(choices=[('0', 'Стажер'), ('1', '1я категория'), ('2', '2я категория'), ('3', '3я категория'), ('4', 'Ведущий')], max_length=1)),
                ('work', models.IntegerField()),
            ],
        ),
    ]
