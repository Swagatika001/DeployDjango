
from django.db import models
from utils.models import AbstractTableMeta


class Lecturer(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()