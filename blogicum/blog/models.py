from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedCreated
from blog.constants import MAX_LENGTH_TITLE, FIELD_LENGTH

User = get_user_model()


class Category(PublishedCreated):
    title = models.CharField(
                             'Заголовок',
                             max_length=MAX_LENGTH_TITLE
                            )
    description = models.TextField('Описание')
    slug = models.SlugField(
                            'Идентификатор',
                            unique=True,
                            help_text=('Идентификатор страницы для URL; '
                                       'разрешены символы латиницы, цифры, '
                                       'дефис и подчёркивание.')
                           )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:FIELD_LENGTH]


class Location(PublishedCreated):
    name = models.CharField(
                            'Название места',
                            max_length=MAX_LENGTH_TITLE
                           )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:FIELD_LENGTH]


class Post(PublishedCreated):
    title = models.CharField(
                             'Заголовок',
                             max_length=MAX_LENGTH_TITLE
                            )
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
                                    'Дата и время публикации',
                                    help_text=('Если установить '
                                               'дату и время в будущем '
                                               '— можно делать отложенные '
                                               'публикации.')
                                   )
    author = models.ForeignKey(
                               User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор публикации'
                               )
    location = models.ForeignKey(
                                 Location,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='posts',
                                 verbose_name='Местоположение'
                                 )
    category = models.ForeignKey(
                                 Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='posts',
                                 verbose_name='Категория'
                                )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:FIELD_LENGTH]
