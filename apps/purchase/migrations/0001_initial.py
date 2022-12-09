# Generated by Django 3.2.16 on 2022-12-09 19:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PackageModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Joined"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Modified"
                    ),
                ),
                ("label", models.CharField(max_length=255, verbose_name="Label")),
                ("price", models.FloatField(verbose_name="Price")),
                ("slug", models.SlugField(verbose_name="Slug")),
                (
                    "books",
                    models.ManyToManyField(
                        related_name="packages",
                        to="book.BookModel",
                        verbose_name="Books",
                    ),
                ),
            ],
            options={
                "verbose_name": "Package",
                "verbose_name_plural": "Packages",
            },
        ),
        migrations.CreateModel(
            name="StoreModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Joined"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("dummy", "Dummy"),
                            ("apple", "Apple"),
                            ("google", "google"),
                        ],
                        max_length=255,
                        verbose_name="Store Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Store",
                "verbose_name_plural": "Stores",
            },
        ),
        migrations.CreateModel(
            name="PurchaseModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Joined"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date Modified"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "approve"),
                            ("refused", "Refused"),
                        ],
                        default="pending",
                        max_length=100,
                        verbose_name="Purchase Status",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="book.bookmodel",
                        verbose_name="Book",
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="purchase.packagemodel",
                        verbose_name="Package",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Purchase",
                "verbose_name_plural": "Purchases",
            },
        ),
    ]
