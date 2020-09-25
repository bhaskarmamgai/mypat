from django.db import models
from subjects.models import TimeStamp


class Exams(TimeStamp):
    code = models.CharField(unique=True, max_length=20, verbose_name="Examination Code")
    name = models.CharField(max_length=100, verbose_name="Name")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.code, self.name)


class SubCategory(TimeStamp):
    name = models.CharField(max_length=100, verbose_name="Name")
    exam = models.ForeignKey(Exams, on_delete=models.PROTECT, related_name="subcategories")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.id, self.name)
