from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    groups = None
    user_permissions = None

    is_premium = models.BooleanField(verbose_name=_("Is Premium"), default=False)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
