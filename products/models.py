from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Категория', max_length=128, unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('На складе', default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
