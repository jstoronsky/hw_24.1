from django.db import models
from users.models import NULLABLE
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='название')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_link = models.CharField(max_length=250, verbose_name='ссылка', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
