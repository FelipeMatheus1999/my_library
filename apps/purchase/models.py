from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.book.models import BookModel
from apps.user.models import UserModel
from utils.abstract_models.base_model import BaseModel


class StoreModel(BaseModel):
    name = models.CharField(verbose_name=_("Store Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class PackageModel(BaseModel):
    label = models.CharField(verbose_name=_("Label"), max_length=255)
    price = models.FloatField(verbose_name=_("Price"))
    slug = models.SlugField(verbose_name=_("Slug"))
    books = models.ManyToManyField(
        BookModel, verbose_name=_("Books"), related_name="packages"
    )

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.slug


class ContractModel(BaseModel):
    receipt = models.TextField(verbose_name=_("Receipt"))
    package = models.ForeignKey(
        PackageModel,
        verbose_name=_("Package"),
        related_name="contracts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    book = models.ForeignKey(
        BookModel,
        verbose_name=_("Book"),
        related_name="contracts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        verbose_name=_("User"),
        related_name="contracts",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Contract")
        verbose_name_plural = _("Contracts")

    def __str__(self):
        if self.book:
            return f"{self.user.username} - {self.book}"

        return f"{self.user.username} - {self.package}"

    def clean(self):
        if not self.book or not self.package:
            ValidationError("Your contract needs a book or a package registered.")
