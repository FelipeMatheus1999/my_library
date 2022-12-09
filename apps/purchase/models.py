from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.book.models import BookModel
from apps.user.models import UserModel
from utils.abstract_models.base_model import BaseModel


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


class StoreModel(BaseModel):
    STORE_CHOICES = (
        ("dummy", "Dummy"),
        ("apple", "Apple"),
        ("google", "google"),
    )

    name = models.CharField(
        verbose_name=_("Store Name"), max_length=255, choices=STORE_CHOICES
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class PurchaseModel(BaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "approve"),
        ("refused", "Refused"),
    )

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
    status = models.CharField(
        verbose_name=_("Purchase Status"),
        choices=STATUS_CHOICES,
        default="pending",
        max_length=100,
    )

    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")

    def __str__(self):
        return f"Purchase from {self.user}"
