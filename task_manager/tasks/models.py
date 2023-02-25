from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120, verbose_name='Загловок')
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание')
    startTime = models.DateTimeField(verbose_name='Дата начала', auto_now_add=True)
    endTime = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания', editable=True)
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
