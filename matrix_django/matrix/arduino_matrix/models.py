from django.db import models

class Matrix(models.Model):
    image = models.JSONField()
