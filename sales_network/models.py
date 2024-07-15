from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=160, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'Название: {self.title}, Модель: {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Link(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    email = models.EmailField(max_length=100, verbose_name='почта', **NULLABLE)
    country = models.CharField(max_length=250, verbose_name='Страна')
    city = models.CharField(max_length=250, verbose_name='Город')
    street = models.CharField(max_length=250, verbose_name='Улица', **NULLABLE)
    house_number = models.PositiveSmallIntegerField(verbose_name='Номер дома', **NULLABLE)
    product = models.ManyToManyField('Product', default=None, verbose_name='Продукт')
    provider = models.ForeignKey('Link', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(default=0, verbose_name='Задолженность', **NULLABLE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'
