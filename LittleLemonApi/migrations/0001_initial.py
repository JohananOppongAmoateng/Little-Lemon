# Generated by Django 4.2.2 on 2023-07-07 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("slug", models.SlugField()),
                ("title", models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(db_index=True, max_length=255)),
                (
                    "price",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
                ),
                ("featured", models.BooleanField(db_index=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LittleLemonApi.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("status", models.BooleanField(db_index=True, default=0)),
                (
                    "total",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
                ),
                ("date", models.DateField(db_index=True)),
                (
                    "delivery_crew",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="delivery_crew",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.SmallIntegerField()),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "menuitem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LittleLemonApi.menuitem",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LittleLemonApi.order",
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "menuitem")},
            },
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.SmallIntegerField()),
                (
                    "unit_price",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
                ),
                (
                    "price",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
                ),
                (
                    "menuitem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LittleLemonApi.menuitem",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("menuitem", "user")},
            },
        ),
    ]