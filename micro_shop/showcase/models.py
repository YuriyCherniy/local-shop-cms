from django.db import models
from django.shortcuts import reverse

from category_manager.models import Category


class Item(models.Model):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['-pub_date']

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,  # TODO Выглядит так, что тут зря SET_NULL, CASCADE подошел бы лучше
        verbose_name='Категория товара',
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=30,
        verbose_name='название',
        help_text='Длинна названия не должна превышать 30 символов.'
    )

    image = models.ImageField(
        upload_to='item_images',
        verbose_name='изображение',  # TODO У тебя в строке ниже записаны все пробелы которые ты использовал для табуляции
        help_text='''Формат изображения должен быть 1×1,
        рекомендуемое разрешение 600×600 пикселей. Размер
        изображения не должен превышать 1 мегабайт.'''
    )

    description = models.TextField(
        blank=True,
        max_length=500,
        verbose_name='описание',
        help_text='Длинна описания не должна превышать 500 символов.'
    )

    price = models.IntegerField(verbose_name='цена')

    is_archived = models.BooleanField(
        default=False,
        choices=[(True, 'Да'), (False, 'Нет')],
        verbose_name='Поместить товар в архив',
        help_text='Архивированные товары не отображаются посетителям сайта.'
    )

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_detail_url', args=[self.pk])
