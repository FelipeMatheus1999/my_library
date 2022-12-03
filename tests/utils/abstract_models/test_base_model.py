from django.db import models
from django.utils import timezone

from utils.abstract_models.base_model import BaseModel


class TestBaseModel:
    @classmethod
    def setup_class(cls):
        cls.model = BaseModel

    def test_parent_class(self):
        assert issubclass(self.model, models.Model)

    def test_is_active_field(self):
        field = self.model._meta.get_field("is_active")

        assert type(field) == models.BooleanField
        assert field.default is True

    def test_date_joined_field(self):
        field = self.model._meta.get_field("date_joined")

        assert type(field) == models.DateTimeField
        assert field.verbose_name == "Date Joined"
        assert field.default == timezone.now

    def test_date_modified_field(self):
        field = self.model._meta.get_field("date_modified")

        assert type(field) == models.DateTimeField
        assert field.verbose_name == "Date Modified"
        assert field.default == timezone.now

    def test_meta_abstract(self):
        assert self.model._meta.abstract is True
