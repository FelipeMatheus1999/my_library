from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.book.models import BookModel


class UserModel(AbstractUser):
    groups = None
    user_permissions = None

    is_premium = models.BooleanField(verbose_name=_("Is Premium"), default=False)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    books = models.ManyToManyField(
        BookModel, verbose_name=_("User Books"), related_name="users"
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
