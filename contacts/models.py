from uuid import uuid4

from django.db import models
import uuid


# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)


class Meta:
    verbose_name_plural = 'contacts'
