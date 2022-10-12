from django.db import models
from django.db.models import JSONField


class Value(models.Model):
    name = models.CharField(max_length=100)
    jsonb = JSONField()

    def __str__(self):
        return self.name
