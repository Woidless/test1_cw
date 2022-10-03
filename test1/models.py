from django.db import models

# Create your models here.

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return 'Post'


class Comment(models.Model):
    
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self) -> str:
        return 'Cooment'

