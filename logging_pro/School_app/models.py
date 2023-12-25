from django.db import models

class School(models.Model):
    name = models.CharField(max_length=20)
    std = models.IntegerField()
    div = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    spl_sub = models.CharField(max_length=20)

