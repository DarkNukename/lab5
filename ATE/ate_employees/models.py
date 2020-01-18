from django.db import models
from uuid import uuid4

# Create your models here.

class ATE_Employees(models.Model):

    kinds_EL = (
        ('0', 'отсутствует'),
        ('1', 'a1'),
        ('2', 'a2'),
        ('3', 'b1'),
        ('4', 'b2'),
        ('5', 'c1'),
        ('6', 'c2'),
    )

    kinds_SK = (
        ('0', 'Стажер'),
        ('1', '1я категория'),
        ('2', '2я категория'),
        ('3', '3я категория'),
        ('4', 'Ведущий'),
    )

    kinds_SP = (
        ('0', 'Монтажник'),
        ('1', 'Физик'),
        ('2', 'Технолог'),
        ('3', 'Программист'),
        ('4', 'Ядерщик'),
        ('5', 'КИП'),
        ('6', 'Электрик'),
    )

    uuid = models.UUIDField(primary_key = True, default = uuid4)
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
    english_level = models.CharField(max_length = 1, choices = kinds_EL)
    specialization = models.CharField(max_length = 1, choices = kinds_SP)
    skill = models.CharField(max_length = 1, choices = kinds_SK)
    work = models.UUIDField(null=True)

    def __str__(self):
        return str(self.uuid)
