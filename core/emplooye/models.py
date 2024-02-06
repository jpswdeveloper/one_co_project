from django.db import models
import uuid
from business.models import Business
from user.models import User


# Create your models here.
class Emplooye(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bussiness = models.ForeignKey(Business, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
