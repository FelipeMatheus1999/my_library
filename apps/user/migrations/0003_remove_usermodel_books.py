# Generated by Django 3.2.16 on 2022-12-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_usermodel_books"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="books",
        ),
    ]
