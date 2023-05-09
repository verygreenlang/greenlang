import uuid

from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    history = HistoricalRecords(inherit=True)
    last_modification = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
