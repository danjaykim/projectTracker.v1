# Generated by Django 5.0.6 on 2024-05-30 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_note"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Note",
        ),
    ]