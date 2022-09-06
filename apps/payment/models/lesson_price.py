from django.db import models
from uuid import uuid4


class PriceOfOneHourLesson(models.Model):
    standard = models.IntegerField()
    premium = models.IntegerField()
    native = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Lesson(models.Model):
    lesson_duration_on_minutes = models.IntegerField()


