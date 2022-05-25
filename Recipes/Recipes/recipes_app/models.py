from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.URLField()

    preparation = models.TextField()

    ingredients = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

