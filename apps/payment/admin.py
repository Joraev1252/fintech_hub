from django.contrib import admin
from apps.payment.models.lesson_price import PriceOfOneHourLesson, Lesson


admin.site.register(PriceOfOneHourLesson)
admin.site.register(Lesson)