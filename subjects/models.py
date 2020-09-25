from django.db import models

# Move it in Common
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subject(TimeStamp):
    code = models.CharField(unique=True, max_length=20, verbose_name="Subject Code")
    name = models.CharField(max_length=100, verbose_name="Name")
    sub_category = models.ForeignKey('exams.SubCategory',on_delete=models.PROTECT,related_name="subjects")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.code, self.name)


class Topics(TimeStamp):
    name = models.CharField(max_length=100, verbose_name="Name")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="topics")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.id, self.name)
