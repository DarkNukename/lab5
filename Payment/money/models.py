from django.db import models
from uuid import uuid4
# Create your models here.

class PayList(models.Model):

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
    skill = models.CharField(max_length = 1, choices = kinds_SK)
    specialization = models.CharField(max_length = 1, choices = kinds_SP)
    coeff = models.CharField(max_length = 10)

    def __str__(self):
        return self.title
