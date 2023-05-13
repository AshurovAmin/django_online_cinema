from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=30)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    year = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    video = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильма'
        verbose_name_plural = 'Фильмы'
        db_table = 'Movie'

