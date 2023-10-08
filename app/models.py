from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    bio = models.TextField('Биография')
    image = models.ImageField('Фото')

    def __str__(self):
        return f'{self.username}'


class Project(models.Model):
    
    title = models.CharField('Название проекта', max_length=256)
    description = models.TextField('Описание проекта', blank=True, null=True)
    start_date = models.DateField('Дата начала', auto_now=True)
    end_date = models.DateField('Дата окончания', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='owned_projects')
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return f'{self.title}'



class Task(models.Model):

    title = models.CharField('Название задачи', max_length=256)
    description = models.TextField('Описание задачи', blank=True, null=True)
    deadline_date = models.DateField('Крайний срока', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Проект')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Назначен на')   
    completed = models.BooleanField('Завершен', default=False)

    def __str__(self):
        return f'{self.title}'
