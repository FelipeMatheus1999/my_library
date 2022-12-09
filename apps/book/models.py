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
    price = models.FloatField(verbose_name=_("Book Price"))
    categories = models.ManyToManyField(
        BookCategoryModel, verbose_name=_("Book Categories"), related_name="books"
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"({self.author} - {self.title})"


class PageModel(BaseModel):
    number = models.SmallIntegerField(verbose_name=_("Page Number"))
    content = models.TextField(verbose_name=_("Page Content"))
    book = models.ForeignKey(
        BookModel,
        verbose_name=_("Book Pages"),
        related_name="pages",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return f"Book page {self.number}"
