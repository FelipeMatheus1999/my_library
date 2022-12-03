from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"), default=timezone.now
    )
    date_modified = models.DateTimeField(
        verbose_name=_("Date Modified"), default=timezone.now
    )

    class Meta:
        abstract = True
