from django.db import models


# Create your models here.
class Flames(models.Model):
    n1 = models.CharField(max_length=100, default='', blank=False)
    n2 = models.CharField(max_length=100, default='', blank=False)
    def __str__(self):
        return str(self.n1) + str(self.n2)