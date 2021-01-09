from django.db import models


# Create your models here.
class UserAccessModel(models.Model):
    source_file = models.CharField(max_length=150)
    target_file = models.CharField(max_length=150)