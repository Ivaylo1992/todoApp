from django.db import models

from todoApp.todos.choices import StateChoices


class Category(models.Model):
    name = models.CharField(
        max_length=15
    )


class Todo(models.Model):
    title = models.CharField(
        max_length=30
    )

    description = models.TextField()

    state = models.BooleanField(
        choices=[
            (True, StateChoices.DONE),
            (False, StateChoices.NOT_DONE)
        ],
        default=False
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )    

    def __str__(self):
        return self.title

