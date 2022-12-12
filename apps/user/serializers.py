from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models import UserModel


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "is_verified",
            "birth_date",
            "country",
            "date_joined",
            "last_login",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"write_only": True},
            "confirm_password": {"read_only": True},
            "is_verified": {"read_only": True},
            "last_login": {"read_only": True},
        }

    @staticmethod
    def _validate_password(data):
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError({"password": _("The passwords doesn't match.")})

    def validate(self, data):
        self._validate_password(data)

        return data

    def save(self):
        validated_data = self.validated_data
        del validated_data["confirm_password"]
