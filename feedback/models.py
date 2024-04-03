from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               verbose_name='Автор')
    description = models.TextField('Отзыв')
    created_at = models.DateTimeField('Дата отзыва', auto_now_add=True)
    stars = models.PositiveSmallIntegerField('Звезды', default=5)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at')

    def __str__(self):
        return description[:30]


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField('Дата отзыва', auto_now_add=True)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,
                               verbose_name='Отзыв', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               verbose_name='Автор')


class Rate(models.Model):
    pass

# Comment.objects.get(id=1).feedback.description
# Feedback.objects.get(id=1).comments
