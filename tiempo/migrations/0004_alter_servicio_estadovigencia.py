# Generated by Django 4.2.6 on 2023-12-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tiempo", "0003_rename_password_confirmation_persona_confirm_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="estadoVigencia",
            field=models.CharField(
                choices=[("vigente", "Vigente"), ("no_vigente", "No vigente")],
                max_length=20,
                verbose_name="Estado",
            ),
        ),
    ]
