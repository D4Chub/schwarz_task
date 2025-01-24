from django.db import models


class Authors(models.Model):
    name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField(
        "Отчество",
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return f"{self.last_name} {self.name}"


class Genres(models.Model):
    name = models.CharField("Название жанра", max_length=50)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    
    def __str__(self):
        return self.name
    

class Books(models.Model):
    name = models.CharField("Название книги", max_length=150)
    author = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="books",
    )
    genre = models.ForeignKey(
        Genres,
        on_delete=models.CASCADE,
        verbose_name="Жанр",
        related_name="books",
    )
    publishing_year = models.IntegerField("Год издания")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    
    def __str__(self):
        return self.name
