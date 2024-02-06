from django.db import models
import uuid
from emplooye.models import Emplooye


# Create your models here.
class Insurance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    emplooye = models.ForeignKey(Emplooye, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=100, null=False)
