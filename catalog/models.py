from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name = 'Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    category = models.CharField(max_length=50, verbose_name='Категория')
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
