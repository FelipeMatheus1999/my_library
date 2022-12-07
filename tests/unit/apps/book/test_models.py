from django.db import models

from apps.book.models import BookCategoryModel, BookModel
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

    def test_page_numbers_field(self):
        field = self.model._meta.get_field("page_numbers")

        assert type(field) == models.SmallIntegerField
        assert field.verbose_name == "Book Page Numbers"

    def test_categories_field(self):
        field = self.model._meta.get_field("categories")

        assert type(field) == models.ManyToManyField
        assert field.related_model == BookCategoryModel
        assert field.verbose_name == "Book Categories"
        assert field.remote_field.related_name == "books"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 9
