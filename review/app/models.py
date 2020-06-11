from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    img = models.FileField(upload_to='products/%Y/%m/%d/')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(verbose_name='Содержание')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]
