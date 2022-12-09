from django.db import models

from apps.user.models import UserModel


class TestUserModel:
    @classmethod
    def setup_class(cls):
        cls.model = UserModel

    def test_str(self):
        user = UserModel(username="Some Username")

        assert str(user) == "Some Username"

    def test_parent_class(self):
        assert issubclass(self.model, models.Model)

    def test_meta_verbose_name(self):
        self.model.verbose_name = "User"

    def test_meta_verbose_name_plural(self):
        self.model.verbose_name = "Users"

    def test_is_verified_field(self):
        field = self.model._meta.get_field("is_verified")

        assert type(field) == models.BooleanField
        assert field.verbose_name == "User Is Verified"
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

    def test_birth_date_field(self):
        field = self.model._meta.get_field("birth_date")

        assert type(field) == models.DateTimeField
        assert field.verbose_name == "Birth Date"
        assert field.null is True
        assert field.blank is True

    def test_country_field(self):
        field = self.model._meta.get_field("country")

        assert type(field) == models.CharField
        assert field.verbose_name == "User Country"
        assert field.null is True
        assert field.blank is True

    def test_length_field(self):
        assert len(self.model._meta.fields) == 14
