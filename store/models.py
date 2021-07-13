from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
