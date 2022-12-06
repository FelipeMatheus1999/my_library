from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.abstract_models.base_model import BaseModel


class BookCategoryModel(BaseModel):
    name = models.CharField(verbose_name=_("Book Category Name"), max_length=255)

    class Meta:
        verbose_name = _("Book Category")
        verbose_name_plural = _("Book Categories")

    def __str__(self):
        return self.name


class BookModel(BaseModel):
    title = models.CharField(verbose_name=_("Book Title"), max_length=255)
    author = models.CharField(verbose_name=_("Book Author"), max_length=255)
    publishing_company = models.CharField(
        verbose_name=_("Book Publishing Company"), max_length=255
    )
    price = models.SmallIntegerField(verbose_name=_("Book Price"))
    page_numbers = models.SmallIntegerField(verbose_name=_("Book Page Numbers"))
    categories = models.ManyToManyField(
        BookCategoryModel, verbose_name=_("Book Categories"), related_name="books"
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"({self.author} - {self.title})"
