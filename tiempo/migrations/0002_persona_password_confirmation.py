# Generated by Django 4.2.7 on 2023-12-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tiempo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="persona",
            name="password_confirmation",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Confirmar Password"
            ),
        ),
    ]