from django.db import models

from apps.book.models import BookModel
from apps.purchase.models import ContractModel, PackageModel, StoreModel
from apps.user.models import UserModel
from utils.abstract_models.base_model import BaseModel


class TestStoreModel:
    @classmethod
    def setup_class(cls):
        cls.model = StoreModel

    def test_str(self):
        store = StoreModel(name="Some Name")

        assert str(store) == "Some Name"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Store"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Stores"

    def test_name_field(self):
        field = self.model._meta.get_field("name")

        assert type(field) == models.CharField
        assert field.verbose_name == "Store Name"
        assert field.max_length == 255

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 5


class TestPackageModel:
    @classmethod
    def setup_class(cls):
        cls.model = PackageModel

    def test_str(self):
        package = PackageModel(slug="some_slug")

        assert str(package) == "some_slug"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Package"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Packages"

    def test_label_field(self):
        field = self.model._meta.get_field("label")

        assert type(field) == models.CharField
        assert field.verbose_name == "Label"
        assert field.max_length == 255

    def test_price_field(self):
        field = self.model._meta.get_field("price")

        assert type(field) == models.FloatField
        assert field.verbose_name == "Price"

    def test_slug_field(self):
        field = self.model._meta.get_field("slug")

        assert type(field) == models.SlugField
        assert field.verbose_name == "Slug"

    def test_books_field(self):
        field = self.model._meta.get_field("books")

        assert type(field) == models.ManyToManyField
        assert field.related_model == BookModel
        assert field.verbose_name == "Books"
        assert field.remote_field.related_name == "packages"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 7


class TestContractModel:
    @classmethod
    def setup_class(cls):
        cls.model = ContractModel

    def test_str_with_package(self):
        user = UserModel()
        package = PackageModel()
        contract = ContractModel(user=user, package=package)

        assert str(contract) == f"{user.username} - {package}"

    def test_str_with_book(self):
        user = UserModel()
        book = BookModel()
        contract = ContractModel(user=user, book=book)

        assert str(contract) == f"{user.username} - {book}"

    def test_parent_class(self):
        assert issubclass(self.model, BaseModel)

    def test_verbose_name(self):
        assert self.model._meta.verbose_name == "Contract"

    def test_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Contracts"

    def test_receipt_field(self):
        field = self.model._meta.get_field("receipt")

        assert type(field) == models.TextField
        assert field.verbose_name == "Receipt"

    def test_package_field(self):
        field = self.model._meta.get_field("package")

        assert type(field) == models.ForeignKey
        assert field.related_model == PackageModel
        assert field.verbose_name == "Package"
        assert field.remote_field.related_name == "contracts"
        assert field.remote_field.on_delete.__name__ == "CASCADE"
        assert field.null is True
        assert field.blank is True

    def test_book_field(self):
        field = self.model._meta.get_field("book")

        assert type(field) == models.ForeignKey
        assert field.related_model == BookModel
        assert field.verbose_name == "Book"
        assert field.remote_field.related_name == "contracts"
        assert field.remote_field.on_delete.__name__ == "CASCADE"
        assert field.null is True
        assert field.blank is True

    def test_user_field(self):
        field = self.model._meta.get_field("user")

        assert type(field) == models.ForeignKey
        assert field.related_model == UserModel
        assert field.verbose_name == "User"
        assert field.remote_field.related_name == "contracts"
        assert field.remote_field.on_delete.__name__ == "CASCADE"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 8
