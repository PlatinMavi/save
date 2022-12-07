from django.db import models
from django.utils import timezone
# Create your models here.
class student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    kayıtsenesi = models.DateTimeField("kayıt tarihi")

    def sınıf(self):
        return timezone.now - self.kayıtsenesi
