from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Производитель")
    model = models.CharField(max_length=50, verbose_name="Модель")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.brand} {self.model}"

    def review_count(self):
        return Review.objects.filter(car=self).count()

    review_count.short_description = "Количество статей"


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Содержание")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Cтатьи"

    def __str__(self):
        return str(self.car) + " " + self.title
