from django.db import models
from jsonfield import JSONField


class SchemaModel(models.Model):
    data = JSONField()
