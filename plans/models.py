from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.title}"

# Create your models here.
