from django.db import models

# Create your models here.

class Articles(models.Model):
    ID = models.AutoField(primary_key=True)
    ph = models.FloatField(max_length=10)
    temp = models.FloatField(max_length=10)
    BOD = models.IntegerField()
    COD = models.IntegerField()
    TSS = models.FloatField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    DO = models.FloatField(max_length=10)
    watercons = models.IntegerField(max_length=10)
    Alkalinity = models.IntegerField(max_length=10)
    EBOD = models.IntegerField()
    ETSS = models.IntegerField()
    ENH = models.FloatField(max_length=10)
    ANO = models.FloatField(max_length=10)
    Eph = models.FloatField(max_length=10)
    FMLSS = models.IntegerField()
    ADO = models.FloatField(max_length=10)
    ANH = models.FloatField(max_length=10)

    def __str__(self):
        return self.title