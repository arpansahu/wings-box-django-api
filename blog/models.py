from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from accounts.models import Account
from core.models import AbstractBaseModel
from core.storage_backends import PublicMediaStorage

class Post(AbstractBaseModel):
    title = models.CharField(max_length=250)
    content = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title