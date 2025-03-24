from django.db import models

class Equipment(models.Model):
    objects     = None
    nome        = models.CharField(max_length=255)


