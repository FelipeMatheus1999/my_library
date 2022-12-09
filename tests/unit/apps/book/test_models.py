from django.db import models

from apps.book.models import BookCategoryModel, BookModel, PageModel
from utils.abstract_models.base_model import BaseModel


class TestBookCategoryModel:
    @classmethod
    def setup_class(cls):
        cls.model = BookCategoryModel

    def test_str(self):
        category = BookCategoryModel(name="Some Name")

        assert str(category) == "Some Name"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Book Category"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Book Categories"

    def test_name_field(self):
        field = self.model._meta.get_field("name")

        assert type(field) == models.CharField
        assert field.verbose_name == "Book Category Name"
        assert field.max_length == 255

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 5


class TestBookModel:
    @classmethod
    def setup_class(cls):
        cls.model = BookModel

    def test_str(self):
        book = BookModel(author="Some Author", title="Some Title")

        assert str(book) == "(Some Author - Some Title)"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Book"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Books"

    def test_title_field(self):
        field = self.model._meta.get_field("title")

        assert type(field) == models.CharField
        assert field.verbose_name == "Book Title"
        assert field.max_length == 255

    def test_author_field(self):
        field = self.model._meta.get_field("author")

        assert type(field) == models.CharField
        assert field.verbose_name == "Book Author"
        assert field.max_length == 255

    def test_publishing_company_field(self):
        field = self.model._meta.get_field("publishing_company")

        assert type(field) == models.CharField
        assert field.verbose_name == "Book Publishing Company"
        assert field.max_length == 255

    def test_price_field(self):
        field = self.model._meta.get_field("price")

        assert type(field) == models.FloatField
        assert field.verbose_name == "Book Price"

    def test_categories_field(self):
        field = self.model._meta.get_field("categories")

        assert type(field) == models.ManyToManyField
        assert field.related_model == BookCategoryModel
        assert field.verbose_name == "Book Categories"
        assert field.remote_field.related_name == "books"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 8


class TestPageModel:
    @classmethod
    def setup_class(cls):
        cls.model = PageModel

    def test_str(self):
        page = PageModel(number=1)

        assert str(page) == "Book page 1"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Page"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Pages"

    def test_number_field(self):
        field = self.model._meta.get_field("number")

        assert type(field) == models.SmallIntegerField
        assert field.verbose_name == "Page Number"

    def test_content_field(self):
        field = self.model._meta.get_field("content")

        assert type(field) == models.TextField
        assert field.verbose_name == "Page Content"

    def test_book_field(self):
        field = self.model._meta.get_field("book")

        assert type(field) == models.ForeignKey
        assert field.related_model == BookModel
        assert field.verbose_name == "Book Pages"
        assert field.remote_field.related_name == "pages"
        assert field.remote_field.on_delete.__name__ == "CASCADE"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 7
