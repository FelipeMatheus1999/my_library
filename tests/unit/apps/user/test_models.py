from django.db import models

from apps.book.models import BookModel
from apps.user.models import UserModel


class TestUserModel:
    @classmethod
    def setup_class(cls):
        cls.model = UserModel

    def test_str(self):
        mock_username = "Some Username"
        user = UserModel(username=mock_username)

        assert str(user) == "Some Username"

    def test_parent_class(self):
        assert issubclass(self.model, models.Model)

    def test_meta_verbose_name(self):
        self.model.verbose_name = "User"

    def test_meta_verbose_name_plural(self):
        self.model.verbose_name = "Users"

    def test_is_premium_field(self):
        field = self.model._meta.get_field("is_premium")

        assert type(field) == models.BooleanField
        assert field.verbose_name == "Is Premium"
        assert field.default is False

    def test_first_name_field(self):
        field = self.model._meta.get_field("first_name")

        assert type(field) == models.CharField
        assert field.verbose_name == "First Name"
        assert field.max_length == 255

    def test_last_name_field(self):
        field = self.model._meta.get_field("last_name")

        assert type(field) == models.CharField
        assert field.verbose_name == "Last Name"
        assert field.max_length == 255

    def test_email_field(self):
        field = self.model._meta.get_field("email")

        assert type(field) == models.EmailField
        assert field.verbose_name == "Email Address"
        assert field.unique is True

    def test_books_field(self):
        field = self.model._meta.get_field("books")

        assert type(field) == models.ManyToManyField
        assert field.related_model == BookModel
        assert field.verbose_name == "User Books"
        assert field.remote_field.related_name == "users"

    def test_length_field(self):
        assert len(self.model._meta.fields) == 12
