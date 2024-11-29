from django.db import models

# Create your models here.
# title - поле для названия фильма,
# description - поле для описание фильма,
# feedback - поле для отзыва.

class Films_info(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма', max_length=1000)
    feedback = models.TextField('Отзыв на фильм', max_length=500)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title