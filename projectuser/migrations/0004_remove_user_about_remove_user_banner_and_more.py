# Generated by Django 5.0.2 on 2024-02-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projectuser", "0003_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="about",
        ),
        migrations.RemoveField(
            model_name="user",
            name="banner",
        ),
        migrations.RemoveField(
            model_name="user",
            name="image",
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(),
        ),
    ]
