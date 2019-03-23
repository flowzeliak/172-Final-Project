from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExerType(models.Model):
    exername=models.CharField(max_length=255)
    exerurl=models.URLField(null=True, blank=True)
    exerscript=models.TextField()

    def __str__(self):
        return self.exername

    class Meta:
        db_table='exertype'

class Exerlog(models.Model):
    entrydate=models.DateField()
    exertype=models.ForeignKey(ExerType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    entrytime=models.CharField(max_length=255)
    caloriesburned=models.CharField(max_length=255)

    def __int__(self):
        return self.entrydate

    class Meta:
        db_table='exerlog'