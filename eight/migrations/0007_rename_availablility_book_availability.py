# Generated by Django 4.2.6 on 2024-04-07 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eight", "0006_rename_name_book_title_borrowedbook_fine_amount_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="availablility",
            new_name="availability",
        ),
    ]
