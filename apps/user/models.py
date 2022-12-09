from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    groups = None
    user_permissions = None

    is_verified = models.BooleanField(verbose_name=_("User Is Verified"), default=False)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    birth_date = models.DateTimeField(
        verbose_name=_("Birth Date"), null=True, blank=True
    )
    country = models.CharField(verbose_name=_("User Country"), null=True, blank=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
